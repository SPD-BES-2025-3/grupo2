import {
  type Movie,
  type Genre,
  type Reservation,
  type Session,
} from "./entities";

export const genres: Genre[] = [
  { id: 1, name: "Comédia" },
  { id: 2, name: "Animação" },
  { id: 3, name: "Ação" },
  { id: 4, name: "Aventura" },
  { id: 5, name: "Crime" },
  { id: 6, name: "Drama" },
  { id: 7, name: "Terror" },
];

export const movies: Movie[] = [
  {
    id: 1,
    title: "Gente Grande",
    duration_min: 120,
    rating: "PG-13",
    genre_ids: [1],
    poster:
      "https://m.media-amazon.com/images/M/MV5BMjA0ODYwNzU5Nl5BMl5BanBnXkFtZTcwNTI1MTgxMw@@._V1_SX300.jpg",
  },
  {
    id: 2,
    title: "Gato de Botas 2: O Último Pedido",
    duration_min: 102,
    rating: "PG",
    genre_ids: [2, 3, 4],
    poster:
      "https://m.media-amazon.com/images/M/MV5BMzg0MWUzMjctYjVlOS00NzVjLWIwZDMtNzg1YzNkYzdjNTMwXkEyXkFqcGc@._V1_SX300.jpg",
  },
  {
    id: 3,
    title: "Psicopata Americano",
    duration_min: 102,
    rating: "R",
    genre_ids: [5, 6, 7],
    poster:
      "https://m.media-amazon.com/images/M/MV5BNzBjM2I5ZjUtNmIzNy00OGNkLWIwZDMtOTAwYWUwMzA2YjdlXkEyXkFqcGc@._V1_SX300.jpg",
  },
];

export const sessions: Session[] = [
  {
    id: 1,
    movie_id: 1,
    start_time: new Date("2025-07-20T20:00:00Z").toISOString(),
    price_per_vehicle: 30.0,
  },
  {
    id: 2,
    movie_id: 2,
    start_time: new Date("2025-07-21T18:30:00Z").toISOString(),
    price_per_vehicle: 25.0,
  },
  {
    id: 3,
    movie_id: 3,
    start_time: new Date("2025-07-22T21:00:00Z").toISOString(),
    price_per_vehicle: 28.0,
  },
];

export const reservations: Reservation[] = [
  {
    id: 1,
    session_id: 1,
    customer_name: "João Silva",
    vehicle_plate: "ABC1D23",
    vehicle_plate_img: "https://via.placeholder.com/150?text=ABC1D23",
  },
  {
    id: 2,
    session_id: 2,
    customer_name: "Maria Oliveira",
    vehicle_plate: "XYZ9Z99",
    vehicle_plate_img: "https://via.placeholder.com/150?text=XYZ9Z99",
  },
  {
    id: 3,
    session_id: 3,
    customer_name: "Carlos Souza",
    vehicle_plate: "JKL3M21",
    vehicle_plate_img: "https://via.placeholder.com/150?text=JKL3M21",
  },
];
