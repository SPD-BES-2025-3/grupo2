export type Genre = {
  id: number;
  name: string;
};

export type Movie = {
  id: number;
  title: string;
  duration_min: number;
  rating: string;
  genre_ids: number[]; // relates to Genre[]
};

export type Session = {
  id: number;
  movie_id: number;
  start_time: string; // ISO string
  price_per_vehicle: number;
};

export type Reservation = {
  id: number;
  session_id: number;
  customer_name: string;
  vehicle_plate: string;
  vehicle_plate_img: string; // can be a base64 or URL string
};
