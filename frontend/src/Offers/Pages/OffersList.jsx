import React, { useEffect, useState } from "react";
import axios from "axios";

export const OfferList = () => {
  const [offers, setOffers] = useState([]);
  const [experienceLevels, setExperienceLevels] = useState([]); // Stan do przechowywania poziomów doświadczenia
  const [isLoading, setIsLoading] = useState(true);
  const [sortBy, setSortBy] = useState("-date_scraped");
  const [experienceLevel, setExperienceLevel] = useState("");

  const orderingOptions = {
    "Newest": "-date_scraped",
    "Oldest": "date_scraped",
    "Highest Salary": "salary__salary_from",
    "Lowest Salary": "-salary__salary_from",
  };

  const loadOffers = () => {
    setIsLoading(true);

    const token = localStorage.getItem("access_token");
    const params = {
      ordering: sortBy,
      experience_level__name: experienceLevel,
    };

    axios
      .get(`http://localhost:8000/offers/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        params: params,
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

  const loadExperienceLevels = () => {
    axios
      .get("http://localhost:8000/offers/experiences/")
      .then((response) => {
        setExperienceLevels(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    loadOffers();
    loadExperienceLevels();

  }, []);

  const handleSortChange = (event) => {
    const newSortBy = event.target.value;
    setSortBy(newSortBy);
    loadOffers();
  };

  const handleExperienceLevelChange = (event) => {
    const newExperienceLevel = event.target.value;
    setExperienceLevel(newExperienceLevel);
    loadOffers();
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

      <label htmlFor="experienceLevel">Experience Level:</label>
      <select id="experienceLevel" onChange={handleExperienceLevelChange} value={experienceLevel}>
        <option value="">All</option>
        {experienceLevels.map((level) => (
          <option key={level.id} value={level.name}>
            {level.name}
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
