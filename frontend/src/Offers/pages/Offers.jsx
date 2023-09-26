import React from "react";
import OfferFilterForm from "../components/OfferFilterForm";
import "../styles/Offers.css";

const OfferPage = () => {
  return (
    <div>
      <h1 className="heading">Wyszukiwarka ofert pracy</h1>
      <OfferFilterForm />
    </div>
  );
};

export default OfferPage;
