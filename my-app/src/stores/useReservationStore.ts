import create from "zustand";
import { type Reservation, type Cliente } from "../types/entities";

type ReservationStore = {
  cliente?: Cliente;
  reservations: Reservation[];
  selectedReservation?: Reservation;

  getReservations: () => Promise<void>;
  getCliente: () => Promise<void>;
  addReservation: (sessionId: string, placa: string) => Promise<void>;
  deleteReservation: (id: string) => Promise<void>;
  selectReservation: (id: string) => void;
  reset: () => void;

  isOpen: boolean;
  open: () => void;
  close: () => void;
};

export const useReservationStore = create<ReservationStore>((set, get) => ({
  cliente: undefined,
  reservations: [],
  selectedReservation: undefined,
  selectedClient: undefined,

  getCliente: async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/clientes/`);
      if (!response.ok)
        throw new Error(`Erro ao buscar cliente: ${response.statusText}`);
      const data: Cliente[] = await response.json();
      set({ cliente: data[0] });
    } catch (error) {
      console.error("Erro ao buscar cliente:", error);
      throw error;
    }
  },

  getReservations: async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/reservas/`);
      if (!response.ok)
        throw new Error(`Erro ao buscar reservas: ${response.statusText}`);
      const data: Reservation[] = await response.json();
      set({ reservations: data });
    } catch (error) {
      console.error("Erro ao buscar reservas:", error);
      throw error;
    }
  },

  addReservation: async (sessionId, placa) => {
    const { cliente } = get();
    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/reservas/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            sessao_id: sessionId,
            cliente_id: cliente?.id,
            placa,
          }),
        }
      );
      if (!response.ok)
        throw new Error(`Erro ao adicionar reserva: ${response.statusText}`);
    } catch (error) {
      console.error("Erro ao adicionar reserva:", error);
      throw error;
    }
  },

  deleteReservation: async (id) => {
    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/reservas/${id}`,
        { method: "DELETE" }
      );
      if (!response.ok)
        throw new Error(`Erro ao deletar reserva: ${response.statusText}`);
    } catch (error) {
      console.error("Erro ao deletar reserva:", error);
      throw error;
    }
  },

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
