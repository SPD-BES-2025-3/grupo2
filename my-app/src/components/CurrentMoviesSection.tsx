import React from "react";
import { useMovieStore } from "../stores/useMovieStore";
import MovieCard from "./MovieCard";

const CurrentMoviesSection: React.FC = () => {
  const { movies, sessions } = useMovieStore((state) => ({
    movies: state.movies,
    sessions: state.sessions,
  }));

  return (
    <div className="current-movies-section">
      <h2>Current Movies</h2>
      <div style={{ display: "flex", gap: "4rem" }}>
        {movies.map((movie) => {
          const movieSessions = sessions.filter((s) => s.movie_id === movie.id);
          return (
            <MovieCard
              key={movie.id}
              movie={movie}
              sessions={movieSessions}
              onReserve={(id: number) => console.log(id)}
            />
          );
        })}
      </div>
    </div>
  );
};

export default CurrentMoviesSection;
