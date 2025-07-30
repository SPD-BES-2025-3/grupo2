import "./App.css";
import CurrentMoviesSection from "./components/CurrentMoviesSection";
import ReservationsSection from "./components/ReservationsSection";
import ReservationModal from "./components/ReservationModal";
import { useReservationStore } from "./stores/useReservationStore";
import { useEffect } from "react";

function App() {
  const { getCliente } = useReservationStore();

  useEffect(() => {
    (async () => {
      try {
        await getCliente();
      } catch (err) {
        console.log(err);
      }
    })();
  }, []);

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
