import React from "react";
import { useReservationStore } from "../stores/useReservationStore";
import { useMovieStore } from "../stores/useMovieStore";

const ReservationsSection: React.FC = () => {
  const { reservations, deleteReservation, open, selectReservation } =
    useReservationStore();
  const { selectSession, sessions, movies } = useMovieStore();

  const handleEdit = (reservationId: number, sessionId: number) => {
    selectReservation(reservationId);
    selectSession(sessionId);
    open();
  };

  const handleDelete = (id: number) => {
    deleteReservation(id);
  };

  return (
    <div
      style={{
        paddingTop: "2rem",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <h2>Reservas</h2>
      {reservations.length === 0 ? (
        <p>Nenhuma reserva feita.</p>
      ) : (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "1rem",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          {reservations.map((reservation) => {
            const session = sessions.find(
              (s) => s.id === reservation.session_id
            );
            const movie = movies.find((m) => m.id === session?.movie_id);
            return (
              <div
                key={reservation.id}
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "space-between",
                  width: "28rem",
                  background: "#666",
                  padding: "1.5rem",
                  borderRadius: "0.5rem",
                }}
              >
                <div style={{ textAlign: "left" }}>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>ID:</strong> {reservation.id}
                  </p>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>Filme:</strong> {movie?.title}
                  </p>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>Sessão:</strong>{" "}
                    {new Date(session?.start_time || "")
                      .toLocaleString()
                      .slice(0, 17)}
                  </p>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>Cliente:</strong> {reservation.customer_name}
                  </p>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>Placa do veículo:</strong>{" "}
                    {reservation.vehicle_plate}
                  </p>
                </div>
                <div style={{ display: "flex", gap: "0.5rem" }}>
                  <button
                    onClick={() =>
                      handleEdit(reservation.id, reservation.session_id)
                    }
                    style={{ height: "fit-content" }}
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(reservation.id)}
                    style={{ height: "fit-content" }}
                  >
                    Deletar
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default ReservationsSection;
