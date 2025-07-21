import create from "zustand";
import { type Reservation } from "../types/entities";

interface ReservationStore {
  reservations: Reservation[];
  selectedReservation: Reservation | null;

  addReservation: (reservation: Reservation) => void;
  updateReservation: (
    id: number,
    updatedReservation: Partial<Reservation>
  ) => void;
  deleteReservation: (id: number) => void;
  selectReservation: (reservation: Reservation | null) => void;

  isOpen: boolean;
  open: () => void;
  close: () => void;
}

export const useReservationStore = create<ReservationStore>((set) => ({
  reservations: [],
  selectedReservation: null,
  addReservation: (reservation) =>
    set((state) => ({
      reservations: [...state.reservations, reservation],
    })),
  updateReservation: (id, updatedReservation) =>
    set((state) => ({
      reservations: state.reservations.map((reservation) =>
        reservation.id === id
          ? { ...reservation, ...updatedReservation }
          : reservation
      ),
    })),
  deleteReservation: (id) =>
    set((state) => ({
      reservations: state.reservations.filter(
        (reservation) => reservation.id !== id
      ),
    })),
  selectReservation: (reservation) => set({ selectedReservation: reservation }),

  isOpen: false,
  open: () => set(() => ({ isOpen: true })),
  close: () => set(() => ({ isOpen: false })),
}));
