import React from "react";
import { type Movie, type Session } from "../types/entities";

type MovieCardProps = {
  movie: Movie;
  sessions: Session[];
  onReserve: (sessionId: number) => void;
};

const MovieCard: React.FC<MovieCardProps> = ({
  movie,
  sessions,
  onReserve,
}) => {
  const movieGenres = movie.genre_ids.map((id) => `${id}`).join(", "); // Replace with actual genre names if available

  return (
    <div
      style={{
        border: "1px",
        borderRadius: "1rem",
        padding: "1rem",
        background: "#666",
      }}
    >
      <h2 className="text-xl font-bold">{movie.title}</h2>
      <p style={{ margin: "0" }}>Duração: {movie.duration_min} minutos</p>
      <p style={{ margin: "0" }}>Classificação: {movie.rating}</p>
      <p style={{ margin: "0" }}>Gênero(s): {movieGenres}</p>
      <h3 className="font-semibold mt-2">Available Sessions:</h3>
      <ul style={{ paddingRight: "1rem" }}>
        {sessions.map((session) => (
          <li key={session.id} className="flex justify-between items-center">
            <span>
              {new Date(session.start_time).toLocaleString()} - $
              {session.price_per_vehicle}
            </span>
            <button
              style={{
                display: "block",
                paddingRight: "0.4rem",
                paddingLeft: "0.4rem",
                paddingTop: "0.1rem",
                paddingBottom: "0.1rem",
              }}
              onClick={() => onReserve(session.id)}
            >
              Reserve
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieCard;
