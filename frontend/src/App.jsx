import React from 'react';
import './App.css';
import {BrowserRouter as Router, Routes, Route } from "react-router-dom";
import OfferPage from './Offers/pages/Offers';
import RegistrationForm from "./Users/RegistationForm";
import RegisterPage from "./Users/pages/RegisterPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<OfferPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </Router>
      
  );
}

export default App;
