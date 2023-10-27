import React, { useEffect, useState } from "react";
import axios from "axios";

export const OfferList = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [sortBy, setSortBy] = useState("-date_scraped");
  const [countries, setCountries] = useState([]);
  const [country, setCountry] = useState("");

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
    };

    if (country) {
      params.localizations__country = country;
    }

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

  const loadCountries = () => {
    axios
      .get("http://localhost:8000/offers/countries/")
      .then((response) => {
        setCountries(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    loadOffers();
  }, [sortBy, country]); // Trigger loadOffers when sortBy or country change

  useEffect(() => {
    loadCountries();
  }, []);

  const handleSortChange = (event) => {
    const newSortBy = event.target.value;
    setSortBy(newSortBy);
  };

  const handleCountryChange = (event) => {
    const newCountry = event.target.value;
    setCountry(newCountry);
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

      <label htmlFor="country">Country:</label>
      <select id="country" onChange={handleCountryChange} value={country}>
        <option value="">All</option>
        {countries.map((country) => (
          <option key={country.country} value={country.country}>
            {country.country}
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
