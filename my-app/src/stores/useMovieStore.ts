import create from "zustand";
import { type Movie, type Genre, type Session } from "../types/entities";
import { genres } from "../types/mocks";

type MovieStore = {
  movies: Movie[];
  genres: Genre[];
  sessions: Session[];
  selectedSession?: Session;

  getMovies: () => Promise<void>;
  getSessions: () => Promise<void>;
  selectSession: (id: number) => void;
};

export const useMovieStore = create<MovieStore>((set) => ({
  movies: [],
  genres,
  sessions: [],
  selectedSession: undefined,

  getMovies: async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/filmes`);
      if (!response.ok)
        throw new Error(`Erro ao buscar filmes: ${response.statusText}`);
      const data: Movie[] = await response.json();
      set({ movies: data });
    } catch (error) {
      console.error("Erro ao buscar filmes:", error);
      throw error;
    }
  },

  getSessions: async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/sessoes`);
      if (!response.ok)
        throw new Error(`Erro ao buscar sessões: ${response.statusText}`);
      const data: Session[] = await response.json();
      set({ sessions: data });
    } catch (error) {
      console.error("Erro ao buscar sessões:", error);
      throw error;
    }
  },

  selectSession: (id) => {
    set((state) => ({
      selectedSession: state.sessions.find((s) => s.id === id),
    }));
  },
}));
