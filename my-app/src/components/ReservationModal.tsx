import React, { useEffect } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import { useReservationStore } from "../stores/useReservationStore";
import { useMovieStore } from "../stores/useMovieStore";

const ReservationModal = () => {
  const { selectedReservation, updateReservation, addReservation } =
    useReservationStore();
  const { sessions } = useMovieStore();

  const [customerName, setCustomerName] = React.useState(
    selectedReservation?.customer_name || ""
  );
  const [vehiclePlate, setVehiclePlate] = React.useState(
    selectedReservation?.vehicle_plate || ""
  );
  const [vehiclePlateImg, setVehiclePlateImg] = React.useState(
    selectedReservation?.vehicle_plate_img || ""
  );
  const [sessionId, setSessionId] = React.useState(
    selectedReservation?.session_id || ""
  );
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  useEffect(() => {
    if (selectedReservation) {
      setCustomerName(selectedReservation.customer_name);
      setVehiclePlate(selectedReservation.vehicle_plate);
      setVehiclePlateImg(selectedReservation.vehicle_plate_img);
      setSessionId(selectedReservation.session_id);
    } else {
      // clearSelectedReservation();
    }
  }, [selectedReservation]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const reservationData = {
      id: selectedReservation ? selectedReservation.id : Date.now(),
      session_id: Number(sessionId),
      customer_name: customerName,
      vehicle_plate: vehiclePlate,
      vehicle_plate_img: vehiclePlateImg,
    };

    if (selectedReservation) {
      updateReservation(selectedReservation.id, reservationData);
    } else {
      addReservation(reservationData);
    }
    // onClose();
  };

  // if (!isOpen) return null;

  const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 400,
    bgcolor: "background.paper",
    border: "2px solid #000",
    boxShadow: 24,
    p: 4,
  };

  return (
    <div className="modal">
      <div className="modal-content">
        {/* <span className="close" onClick={onClose}> */}
        <span className="close">&times;</span>
        <h2>{selectedReservation ? "Edit Reservation" : "New Reservation"}</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Customer Name</label>
            <input
              type="text"
              value={customerName}
              onChange={(e) => setCustomerName(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Vehicle Plate</label>
            <input
              type="text"
              value={vehiclePlate}
              onChange={(e) => setVehiclePlate(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Vehicle Plate Image</label>
            <input
              type="text"
              value={vehiclePlateImg}
              onChange={(e) => setVehiclePlateImg(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Session</label>
            <select
              value={sessionId}
              onChange={(e) => setSessionId(e.target.value)}
              required
            >
              <option value="">Select a session</option>
              {sessions.map((session) => (
                <option key={session.id} value={session.id}>
                  {session.start_time} - ${session.price_per_vehicle}
                </option>
              ))}
            </select>
          </div>
          <button type="submit">
            {selectedReservation ? "Update Reservation" : "Reserve"}
          </button>
        </form>
      </div>

      <div>
        <Button onClick={handleOpen}>Open modal</Button>
        <Modal
          open={open}
          onClose={handleClose}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <Box sx={style}>
            <Typography id="modal-modal-title" variant="h6" component="h2">
              Text in a modal
            </Typography>
            <Typography id="modal-modal-description" sx={{ mt: 2 }}>
              Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
            </Typography>
          </Box>
        </Modal>
      </div>
    </div>
  );
};

export default ReservationModal;
