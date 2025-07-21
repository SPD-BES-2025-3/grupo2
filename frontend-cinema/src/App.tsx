import React from 'react';
import CurrentMoviesSection from './components/CurrentMoviesSection';
import ReservationsSection from './components/ReservationsSection';

const App: React.FC = () => {
  return (
    <div className="app-container">
      <h1>Drive-In Cinema Reservations</h1>
      <CurrentMoviesSection />
      <ReservationsSection />
    </div>
  );
};

export default App;