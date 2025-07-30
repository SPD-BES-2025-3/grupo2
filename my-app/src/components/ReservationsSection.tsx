import React, { useEffect } from "react";
import { useReservationStore } from "../stores/useReservationStore";
import { useMovieStore } from "../stores/useMovieStore";

const ReservationsSection: React.FC = () => {
  const {
    reservations,
    deleteReservation,
    open,
    selectReservation,
    getReservations,
  } = useReservationStore();
  const { selectSession, sessions, movies } = useMovieStore();

  const handleEdit = (reservationId: string, sessionId: string) => {
    selectReservation(reservationId);
    selectSession(sessionId);
    open();
  };

  const handleDelete = (id: string) => {
    deleteReservation(id);
  };

  useEffect(() => {
    (async () => {
      try {
        await getReservations();
      } catch (err) {
        console.log(err);
      }
    })();
  }, []);

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
              (s) => s.id === reservation.sessao_id
            );
            const movie = movies.find((m) => m.id === session?.filme_id);
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
                    <strong>Filme:</strong> {movie?.titulo}
                  </p>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>Sessão:</strong> {session?.data}{" "}
                    {session?.hora.slice(0, 5)}
                  </p>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>Cliente:</strong> {reservation.cliente_id}
                  </p>
                  <p style={{ width: "fit-content", margin: "0" }}>
                    <strong>Placa do veículo:</strong> {reservation.placa}
                  </p>
                </div>
                <div style={{ display: "flex", gap: "0.5rem" }}>
                  <button
                    onClick={() =>
                      handleEdit(reservation.id, reservation.sessao_id)
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
