# Frontend Cinema

This project is a drive-in cinema system built with React and TypeScript. It allows users to view current movies, make reservations, and manage their bookings.

## Project Structure

```
frontend-cinema
├── src
│   ├── components
│   │   ├── CurrentMoviesSection.tsx
│   │   ├── ReservationsSection.tsx
│   │   ├── ReservationModal.tsx
│   │   └── MovieCard.tsx
│   ├── stores
│   │   ├── useMovieStore.ts
│   │   └── useReservationStore.ts
│   ├── types
│   │   └── entities.ts
│   ├── App.tsx
│   ├── index.tsx
│   └── styles
│       └── main.css
├── public
│   └── index.html
├── package.json
├── tsconfig.json
└── README.md
```

## Features

- **Current Movies Section**: Displays a list of movies currently being shown with details such as title, duration, rating, genres, and available sessions. Each session has a "Reserve" button that opens a modal form.
- **Reservations Section**: Shows a list of reservations made by customers, including customer name, vehicle plate and vehicle plate image. Each reservation has "Edit" and "Delete" actions.

- **Reservation Modal**: A form for creating or editing reservations, including fields for customer name, vehicle plate, vehicle plate image and session selection.

## Technologies Used

- React
- TypeScript
- Zustand for state management
- CSS for styling (custom styles can be added in `src/styles/main.css`)

## Setup Instructions

1. Clone the repository:

   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```
   cd frontend-cinema
   ```

3. Install dependencies:

   ```
   npm install
   ```

4. Start the development server:

   ```
   npm start
   ```

5. Open your browser and go to `http://localhost:3000` to view the application.

## Usage

- View the current movies and their available sessions.
- Make reservations by clicking the "Reserve" button on the desired session.
- Manage your reservations in the Reservations Section, where you can edit or delete them.

## Contributing

Feel free to submit issues or pull requests for any improvements or features you would like to see in this project.
