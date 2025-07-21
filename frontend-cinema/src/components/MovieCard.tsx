import React from "react";
import { Movie, Session } from "../types/entities";

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
  const movieGenres = movie.genre_ids.map((id) => `Genre ${id}`).join(", "); // Replace with actual genre names if available

  return (
    <div className="border rounded-lg p-4 m-2 shadow-md">
      <h2 className="text-xl font-bold">{movie.title}</h2>
      <p>Duration: {movie.duration_min} minutes</p>
      <p>Rating: {movie.rating}</p>
      <p>Genres: {movieGenres}</p>
      <h3 className="font-semibold mt-2">Available Sessions:</h3>
      <ul>
        {sessions.map((session) => (
          <li key={session.id} className="flex justify-between items-center">
            <span>
              {new Date(session.start_time).toLocaleString()} - $
              {session.price_per_vehicle}
            </span>
            <button
              className="bg-blue-500 text-white px-2 py-1 rounded"
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
