import React from "react";
import { useReservationStore } from "../stores/useReservationStore";
import { type Reservation } from "../types/entities";

const ReservationsSection: React.FC = () => {
  const { reservations, deleteReservation } = useReservationStore();

  const handleEdit = (reservation: Reservation) => {
    // setEditingReservation(reservation);
    console.log(reservation);
  };

  const handleDelete = (id: number) => {
    deleteReservation(id);
  };

  return (
    <div style={{ paddingTop: "2rem" }}>
      <h2>Reservas</h2>
      {reservations.length === 0 ? (
        <p>Nenhuma reserva feita.</p>
      ) : (
        <ul>
          {reservations.map((reservation) => (
            <li key={reservation.id} className="reservation-item">
              <div>
                <p>Cliente: {reservation.customer_name}</p>
                <p>Placa do veículo: {reservation.vehicle_plate}</p>
                <img
                  src={reservation.vehicle_plate_img}
                  alt="Vehicle Plate"
                  className="vehicle-image"
                />
              </div>
              <div className="actions">
                <button onClick={() => handleEdit(reservation)}>Edit</button>
                <button onClick={() => handleDelete(reservation.id)}>
                  Delete
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ReservationsSection;
