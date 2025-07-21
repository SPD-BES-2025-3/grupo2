import {
  type Movie,
  type Genre,
  type Reservation,
  type Session,
} from "./entities";

export const genres: Genre[] = [
  { id: 1, name: "Ação" },
  { id: 2, name: "Comédia" },
  { id: 3, name: "Drama" },
];

export const movies: Movie[] = [
  {
    id: 1,
    title: "Missão Explosiva",
    duration_min: 120,
    rating: "PG-13",
    genre_ids: [1],
  },
  {
    id: 2,
    title: "Rindo à Toa",
    duration_min: 95,
    rating: "PG",
    genre_ids: [2],
  },
  {
    id: 3,
    title: "Lágrimas do Amanhã",
    duration_min: 110,
    rating: "PG-13",
    genre_ids: [3],
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
