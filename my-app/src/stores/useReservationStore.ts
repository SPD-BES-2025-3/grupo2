import create from "zustand";
import { type Reservation } from "../types/entities";

type ReservationStore = {
  reservations: Reservation[];
  selectedReservation?: Reservation;

  addReservation: (reservation: Reservation) => void;
  updateReservation: (id: number, updatedReservation: Reservation) => void;
  deleteReservation: (id: number) => void;
  selectReservation: (id: number) => void;
  reset: () => void;

  isOpen: boolean;
  open: () => void;
  close: () => void;
};

export const useReservationStore = create<ReservationStore>((set) => ({
  reservations: [],
  selectedReservation: undefined,
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
  selectReservation: (id) => {
    set((state) => ({
      selectedReservation: state.reservations.find((s) => s.id === id),
    }));
  },
  reset: () => {
    set({ selectedReservation: undefined });
  },

  isOpen: false,
  open: () => set(() => ({ isOpen: true })),
  close: () => set(() => ({ isOpen: false })),
}));
