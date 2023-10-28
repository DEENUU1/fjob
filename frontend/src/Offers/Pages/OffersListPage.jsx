import React, { useEffect, useState } from "react";
import axios from "axios";
import {OfferList} from "../Components/OfferList.jsx";

export const OffersListPage = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const loadOffers = () => {
    setIsLoading(true);

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
        setIsLoading(false);
      });
  };

  useEffect(() => {
    loadOffers();
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>

      <OfferList offers={offers}/>
    </div>
  );
};