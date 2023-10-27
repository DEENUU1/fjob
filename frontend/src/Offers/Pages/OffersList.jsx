import React, { useEffect, useState } from "react";
import axios from "axios";

export const OfferList = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    axios
      .get(`http://localhost:8000/offers/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        setOffers(response.data.results);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <ul>
      {offers.map((offer) => (
        <li key={offer.id}>
          {offer.title}
        </li>
      ))}
    </ul>
  );
};
