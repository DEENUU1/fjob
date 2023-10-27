import React, { useEffect, useState } from "react";
import axios from "axios";

export const OfferList = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [sortBy, setSortBy] = useState("-date_scraped");

  const orderingOptions = {
    "Newest": "-date_scraped",
    "Oldest": "date_scraped",
    "Highest Salary": "salary__salary_from",
    "Lowest Salary": "-salary__salary_from",
  };

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    axios
      .get(`http://localhost:8000/offers/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        params: {
          ordering: sortBy,
        },
      })
      .then((response) => {
        setOffers(response.data.results);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  }, [sortBy]);

  const handleSortChange = (event) => {
    const newSortBy = event.target.value;
    setSortBy(newSortBy);
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <label htmlFor="sort">Sort by:</label>
      <select id="sort" onChange={handleSortChange} value={sortBy}>
        {Object.entries(orderingOptions).map(([label, value]) => (
          <option key={value} value={value}>
            {label}
          </option>
        ))}
      </select>
      <ul>
        {offers.map((offer) => (
          <li key={offer.id}>{offer.title}</li>
        ))}
      </ul>
    </div>
  );
};
