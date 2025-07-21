import create from "zustand";
import { Movie, Genre, Session } from "../types/entities";
import { genres, movies, sessions } from "../types/mocks";

type MovieStore = {
  movies: Movie[];
  genres: Genre[];
  sessions: Session[];
  addMovie: (movie: Movie) => void;
  updateMovie: (id: number, updatedMovie: Partial<Movie>) => void;
  deleteMovie: (id: number) => void;
  addSession: (session: Session) => void;
  updateSession: (id: number, updatedSession: Partial<Session>) => void;
  deleteSession: (id: number) => void;
};

export const useMovieStore = create<MovieStore>((set) => ({
  movies,
  genres,
  sessions,
  addMovie: (movie) => set((state) => ({ movies: [...state.movies, movie] })),
  updateMovie: (id, updatedMovie) =>
    set((state) => ({
      movies: state.movies.map((movie) =>
        movie.id === id ? { ...movie, ...updatedMovie } : movie
      ),
    })),
  deleteMovie: (id) =>
    set((state) => ({
      movies: state.movies.filter((movie) => movie.id !== id),
    })),
  addSession: (session) =>
    set((state) => ({ sessions: [...state.sessions, session] })),
  updateSession: (id, updatedSession) =>
    set((state) => ({
      sessions: state.sessions.map((session) =>
        session.id === id ? { ...session, ...updatedSession } : session
      ),
    })),
  deleteSession: (id) =>
    set((state) => ({
      sessions: state.sessions.filter((session) => session.id !== id),
    })),
}));
