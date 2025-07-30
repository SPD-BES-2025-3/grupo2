import React, { useEffect } from "react";
import { useMovieStore } from "../stores/useMovieStore";
import MovieCard from "./MovieCard";
import { useReservationStore } from "../stores/useReservationStore";

const CurrentMoviesSection: React.FC = () => {
  const { movies, sessions, getMovies } = useMovieStore((state) => ({
    movies: state.movies,
    sessions: state.sessions,
    getMovies: state.getMovies,
  }));
  const { open } = useReservationStore();
  const { selectSession } = useMovieStore();

  useEffect(() => {
    (async () => {
      try {
        await getMovies();
      } catch (err) {
        console.log(err);
      }
    })();
  }, []);

  return (
    <div className="current-movies-section">
      <h2>Filmes em Cartaz</h2>
      <div style={{ display: "flex", gap: "4rem" }}>
        {movies.map((movie) => {
          const movieSessions = sessions.filter((s) => s.movie_id === movie.id);
          return (
            <MovieCard
              key={movie.id}
              movie={movie}
              sessions={movieSessions}
              onReserve={(id) => {
                selectSession(id);
                open();
              }}
            />
          );
        })}
      </div>
    </div>
  );
};

export default CurrentMoviesSection;
