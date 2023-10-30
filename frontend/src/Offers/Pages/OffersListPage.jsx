import React, { useEffect, useState } from "react";
import axios from "axios";
import { OfferList } from "../Components/OfferList.jsx";

export const OffersListPage = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [sortOption, setSortOption] = useState("");
  const [query, setQuery] = useState("");
  const token = localStorage.getItem("access_token");
  const sortUrl = sortOption ? `&ordering=${sortOption}` : "";
  const queryUrl = query ? `&search=${query}` : "";

  const loadOffers = () => {
    setIsLoading(true);

    axios
      .get(`http://localhost:8000/offers/?${sortUrl}${queryUrl}`, {
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
  }, [sortOption, query]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    setQuery(e.currentTarget.elements.query.value)
  }

  return (
    <div>
      <div className="search-container">
        <form className="search-form" onSubmit={handleSubmit}>
          <input id="query" type="text" name="query"  placeholder="Search..." />
          <button type="submit">Search</button>
        </form>
      </div>
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
