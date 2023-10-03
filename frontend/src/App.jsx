import React from 'react';
import './App.css';
import {BrowserRouter as Router, Routes, Route } from "react-router-dom";
import OfferPage from './Offers/pages/Offers';
import RegisterPage from "./Users/pages/RegisterPage";
import LoginPage from "./Users/pages/LoginPage";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<OfferPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </Router>
      
  );
}

export default App;
