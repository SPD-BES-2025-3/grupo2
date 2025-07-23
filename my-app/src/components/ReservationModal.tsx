import React, { useEffect } from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import { useReservationStore } from "../stores/useReservationStore";
import { useMovieStore } from "../stores/useMovieStore";
import MovieCard from "./MovieCard";

const ReservationModal = () => {
  const {
    selectedReservation,
    updateReservation,
    addReservation,
    isOpen,
    close,
  } = useReservationStore();
  const { sessions, movies, selectedSession } = useMovieStore();
  console.log(sessions);
  const movie = movies.find((m) => m.id === selectedSession?.movie_id);

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
    close();
  };

  return (
    <Modal open={isOpen} onClose={close}>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          position: "absolute",
          padding: 4,
          borderRadius: "2rem",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          bgcolor: "background.paper",
          border: "2px solid #000",
          boxShadow: 24,
        }}
      >
        <h2 className="modalText" style={{ marginTop: "0" }}>
          {selectedReservation ? "Editar Reserva" : "Nova Reserva"}
        </h2>
        <div style={{ display: "flex", gap: "3rem" }}>
          {movie && <MovieCard movie={movie} />}
          <form onSubmit={handleSubmit} style={{ padding: "1rem" }}>
            <p className="modalText" style={{ fontSize: "1.1rem" }}>
              <span style={{ fontWeight: "500" }}>Horário: </span>
              {new Date(selectedSession?.start_time || "").toLocaleString()} -
              <span style={{ fontWeight: "500" }}>Preço: </span>$
              {selectedSession?.price_per_vehicle}
            </p>
            <div style={{ display: "flex", gap: "1rem" }}>
              <div>
                <label
                  className="modalText"
                  style={{ display: "block", fontWeight: "500" }}
                >
                  Nome
                </label>
                <input
                  type="text"
                  value={customerName}
                  onChange={(e) => setCustomerName(e.target.value)}
                  required
                  style={{ padding: "0.2rem", fontSize: "0.85rem" }}
                />
              </div>
              <div>
                <label
                  className="modalText"
                  style={{ display: "block", fontWeight: "500" }}
                >
                  Placa do veículo
                </label>
                <input
                  type="text"
                  value={vehiclePlate}
                  onChange={(e) => setVehiclePlate(e.target.value)}
                  required
                />
              </div>
            </div>
            <div
              style={{
                display: "flex",
                justifyContent: "flex-end",
                marginTop: "1.5rem",
              }}
            >
              <button
                type="submit"
                style={{
                  alignSelf: "flex-end",
                  placeSelf: "end",
                  justifySelf: "end",
                }}
              >
                {selectedReservation ? "Update Reservation" : "Reserve"}
              </button>
            </div>
          </form>
        </div>
      </Box>
    </Modal>
  );
};

export default ReservationModal;
