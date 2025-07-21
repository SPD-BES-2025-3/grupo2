import "./App.css";
import CurrentMoviesSection from "./components/CurrentMoviesSection";
import ReservationsSection from "./components/ReservationsSection";
import ReservationModal from "./components/ReservationModal";

function App() {
  return (
    <>
      <h1>Drive-In Cinema</h1>
      <CurrentMoviesSection />
      <ReservationsSection />
      <ReservationModal />
    </>
  );
}

export default App;
