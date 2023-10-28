import React, { useEffect, useState } from "react";
import axios from "axios";
import {OfferList} from "../Components/OfferList.jsx";

export const OffersListPage = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [sortBy, setSortBy] = useState("-date_scraped");
  const [countries, setCountries] = useState([]);
  const [country, setCountry] = useState("");
  const [isRemote, setIsRemote] = useState(false);
  const [isHybrid, setIsHybrid] = useState(false);

  const orderingOptions = {
    "Newest": "-date_scraped",
    "Oldest": "date_scraped",
    "Highest Salary": "salary__salary_from",
    "Lowest Salary": "-salary__salary_from",
  };

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