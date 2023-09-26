import './App.css';
import {BrowserRouter as Router, Routes, Route } from "react-router-dom";
import OfferPage from './Offers/pages/Offers';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<OfferPage />} />
      </Routes>
    </Router>
      
  );
}

export default App;
