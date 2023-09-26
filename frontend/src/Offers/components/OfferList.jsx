// OffersList.js
import React, { useState, useEffect } from "react";
import OfferFilterForm from "./OfferFilterForm";
import OfferCard from "./OfferCard";

const OffersList = () => {
  const [offers, setOffers] = useState([]);

  const fetchOffers = async (formData) => {
    setOffers(formData);
  };

  useEffect(() => {
  }, []);

  return (
    <div>
      <OfferFilterForm onSubmit={fetchOffers} />
      <ul>
        {offers.map((offer) => (
          <OfferCard key={offer.id} offer={offer} />
        ))}
      </ul>
    </div>
  );
};

export default OffersList;
