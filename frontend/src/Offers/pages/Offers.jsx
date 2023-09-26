import React from "react";
import OfferFilterForm from "../components/OfferFilterForm";
import "../styles/Offers.css";
import OffersList from "../components/OfferList";

const OfferPage = () => {
  return (
    <div>
      <h1 className="heading">Search for job offers</h1>
      <OffersList />
    </div>
  );
};

export default OfferPage;
