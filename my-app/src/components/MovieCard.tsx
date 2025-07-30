import React from "react";
import { type Movie, type Session } from "../types/entities";

type MovieCardProps = {
  movie: Movie;
  sessions: Session[];
  onReserve: (sessionId: string) => void;
};

const MovieCard: React.FC<MovieCardProps> = ({
  movie,
  sessions,
  onReserve,
}) => {
  return (
    <div
      style={{
        border: "1px",
        borderRadius: "1rem",
        padding: "1rem",
        background: "#666",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "space-between",
        flex: "1",
      }}
    >
      <img
        src={movie.poster}
        style={{
          width: "200px",
          height: "300px",
          objectFit: "cover",
          borderRadius: "0.5rem",
        }}
      />
      <h2 style={{ maxWidth: "70%" }}>{movie.titulo}</h2>
      <div>
        <h3 style={{ marginTop: "0" }}>Sessões disponíveis:</h3>
        <ul style={{ paddingRight: "1rem", marginTop: "0" }}>
          {sessions.map((session) => (
            <li key={session.id} className="flex justify-between items-center">
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
                {session.data} ({session.hora.slice(0, 5)}) - $
                {session.preco_por_veiculo.toFixed(2).replace(".", ",")}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default MovieCard;
