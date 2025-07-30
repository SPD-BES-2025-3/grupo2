import React from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import { useReservationStore } from "../stores/useReservationStore";
import { useMovieStore } from "../stores/useMovieStore";

const ReservationModal = () => {
  const { selectedReservation, addReservation, isOpen, close, reset } =
    useReservationStore();
  const { movies, selectedSession } = useMovieStore();
  const movie = movies.find((m) => m.id === selectedSession?.filme_id);
  const genres_names = movie?.generos.join(", ");

  const [customerName, setCustomerName] = React.useState(
    selectedReservation?.cliente_id || ""
  );
  const [vehiclePlate, setVehiclePlate] = React.useState(
    selectedReservation?.placa || ""
  );

  // useEffect(() => {
  //   if (selectedReservation) {
  //     setCustomerName(selectedReservation.customer_name);
  //     setVehiclePlate(selectedReservation.vehicle_plate);
  //   }
  // }, [selectedReservation]);

  const handleClose = () => {
    reset();
    setCustomerName("");
    setVehiclePlate("");
    close();
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const reservationData = {
      id: selectedReservation ? selectedReservation.id : Date.now(),
      sessao_id: selectedSession?.id || "",
      customer_name: customerName,
      vehicle_plate: vehiclePlate,
      vehicle_plate_img: "",
    };

    if (selectedReservation) {
      // updateReservation(selectedReservation.id, reservationData);
    } else {
      addReservation(reservationData.sessao_id, "1");
    }
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
          {selectedReservation ? "Editar Reserva" : "Nova Reserva"}
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
            <div style={{ display: "flex", gap: "1rem" }}>
              <div>
                <label
                  style={{
                    display: "block",
                    fontWeight: "500",
                    marginBottom: "0.2rem",
                  }}
                >
                  Nome
                </label>
                <input
                  type="text"
                  value={customerName}
                  onChange={(e) => setCustomerName(e.target.value)}
                  required
                  style={{
                    padding: "0.25rem",
                    fontSize: "0.9rem",
                    borderRadius: "0.25rem",
                  }}
                />
              </div>
              <div>
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
                  style={{
                    padding: "0.25rem",
                    fontSize: "0.9rem",
                    borderRadius: "0.25rem",
                  }}
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
