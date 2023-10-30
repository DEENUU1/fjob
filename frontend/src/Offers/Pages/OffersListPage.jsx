import React, { useEffect, useState } from "react";
import axios from "axios";
import { OfferList } from "../Components/OfferList.jsx";

export const OffersListPage = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [sortOption, setSortOption] = useState("");
  const token = localStorage.getItem("access_token");

  const loadOffers = () => {
    setIsLoading(true);

    const sortUrl = sortOption ? `&ordering=${sortOption}` : "";

    axios
      .get(`http://localhost:8000/offers/?${sortUrl}`, {
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
  }, [sortOption]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div className="sort-container">
        <select value={sortOption} onChange={(e) => setSortOption(e.target.value)}>
          <option value="">Sort by</option>
          <option value="-date_scraped">Newest</option>
          <option value="date_scraped">Oldest</option>
          <option value="-salary__salary_from">Salary highest</option>
          <option value="salary__salary_from">Salary lowest</option>
        </select>
      </div>
      <OfferList offers={offers} />
    </div>
  );
};
