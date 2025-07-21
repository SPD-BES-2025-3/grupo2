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
    <div className="reservations-section">
      <h2>Reservations</h2>
      {reservations.length === 0 ? (
        <p>No reservations made yet.</p>
      ) : (
        <ul>
          {reservations.map((reservation) => (
            <li key={reservation.id} className="reservation-item">
              <div>
                <p>Customer Name: {reservation.customer_name}</p>
                <p>Vehicle Plate: {reservation.vehicle_plate}</p>
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
