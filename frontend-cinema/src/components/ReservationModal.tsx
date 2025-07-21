import React, { useEffect } from "react";
import { useReservationStore } from "../stores/useReservationStore";
import { useMovieStore } from "../stores/useMovieStore";

const ReservationModal: React.FC<{ isOpen: boolean; onClose: () => void }> = ({
  isOpen,
  onClose,
}) => {
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
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>
          &times;
        </span>
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
    </div>
  );
};

export default ReservationModal;
