import create from "zustand";
import { type Movie, type Session } from "../types/entities";

type MovieStore = {
  movies: Movie[];
  sessions: Session[];
  selectedSession?: Session;

  getMovies: () => Promise<void>;
  getSessions: () => Promise<void>;
  selectSession: (id: string) => void;
};

export const useMovieStore = create<MovieStore>((set) => ({
  movies: [],
  sessions: [],
  selectedSession: undefined,

  getMovies: async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/filmes/`);
      if (!response.ok)
        throw new Error(`Erro ao buscar filmes: ${response.statusText}`);
      const data: Movie[] = await response.json();
      for (const movie of data) {
        if (movie.titulo === "Gente Grande")
          movie.poster =
            "https://m.media-amazon.com/images/M/MV5BMjA0ODYwNzU5Nl5BMl5BanBnXkFtZTcwNTI1MTgxMw@@._V1_SX300.jpg";
        if (movie.titulo === "Gato de Botas 2: O Último Pedido")
          movie.poster =
            "https://m.media-amazon.com/images/M/MV5BMzg0MWUzMjctYjVlOS00NzVjLWIwZDMtNzg1YzNkYzdjNTMwXkEyXkFqcGc@._V1_SX300.jpg";
        if (movie.titulo === "Psicopata Americano")
          movie.poster =
            "https://m.media-amazon.com/images/M/MV5BNzBjM2I5ZjUtNmIzNy00OGNkLWIwZDMtOTAwYWUwMzA2YjdlXkEyXkFqcGc@._V1_SX300.jpg";
      }
      set({ movies: data });
    } catch (error) {
      console.error("Erro ao buscar filmes:", error);
      throw error;
    }
  },

  getSessions: async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/sessoes/`);
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
