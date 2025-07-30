import React, { useEffect } from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import { useReservationStore } from "../stores/useReservationStore";
import { useMovieStore } from "../stores/useMovieStore";

const ReservationModal = () => {
  const {
    selectedReservation,
    addReservation,
    isOpen,
    close,
    reset,
    getReservations,
  } = useReservationStore();
  const { movies, selectedSession } = useMovieStore();
  const movie = movies.find((m) => m.id === selectedSession?.filme_id);
  const genres_names = movie?.generos.join(", ");

  const [vehiclePlate, setVehiclePlate] = React.useState(
    selectedReservation?.placa || ""
  );

  useEffect(() => {
    if (selectedReservation) {
      setVehiclePlate(selectedReservation.placa);
    }
  }, [selectedReservation]);

  const handleClose = () => {
    reset();
    setVehiclePlate("");
    close();
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await addReservation(selectedSession?.id || "", vehiclePlate);
    await getReservations();
    handleClose();
  };

  return (
    <Modal open={isOpen} onClose={handleClose}>
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
          bgcolor: "#666",
          border: "2px solid #fff",
          boxShadow: 24,
        }}
      >
        <p style={{ marginTop: "0", fontSize: "2rem", fontWeight: "700" }}>
          {selectedReservation ? "Ver Reserva" : "Nova Reserva"}
        </p>
        <div style={{ display: "flex", gap: "3rem" }}>
          <img src={movie?.poster} style={{ borderRadius: "0.5rem" }} />
          <form onSubmit={handleSubmit} style={{ padding: "1rem" }}>
            <h2>{movie?.titulo}</h2>
            <p style={{ margin: "0" }}>
              Duração: {movie?.duracao_minutos} minutos
            </p>
            <p style={{ margin: "0" }}>
              Classificação: {movie?.classificacao_indicativa}
            </p>
            <p style={{ margin: "0" }}>Gênero(s): {genres_names}</p>
            <p style={{ fontSize: "1.1rem" }}>
              <span style={{ fontWeight: "500" }}>Horário: </span>
              {selectedSession?.data} {selectedSession?.hora.slice(0, 5)} -
              <span style={{ fontWeight: "500" }}> Preço: </span>$
              {selectedSession?.preco_por_veiculo.toFixed(2).replace(".", ",")}
            </p>
            <label
              style={{
                display: "block",
                fontWeight: "500",
                marginBottom: "0.2rem",
              }}
            >
              Placa do veículo
            </label>
            <input
              type="text"
              value={vehiclePlate}
              onChange={(e) => setVehiclePlate(e.target.value)}
              required
              disabled={!!selectedReservation}
              style={{
                padding: "0.25rem",
                fontSize: "0.9rem",
                borderRadius: "0.25rem",
              }}
            />
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
                  display: selectedReservation ? "none" : "block",
                  alignSelf: "flex-end",
                  placeSelf: "end",
                  justifySelf: "end",
                }}
              >
                Reservar
              </button>
            </div>
          </form>
        </div>
      </Box>
    </Modal>
  );
};

export default ReservationModal;
