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
    const params = {
      ordering: sortBy,
    };

    if (country) {
      params.localizations__country = country;
    }

    if (isRemote) {
      params.is_remote = true;
    }

    if (isHybrid) {
      params.is_hybrid = true;
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
        console.log(response.data.results);
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
  }, [sortBy, country, isRemote, isHybrid]);

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

  const handleRemoteChange = (event) => {
    const isRemoteValue = event.target.checked;
    setIsRemote(isRemoteValue);
  };

  const handleHybridChange = (event) => {
    const isHybridValue = event.target.checked;
    setIsHybrid(isHybridValue);
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

      <label>
        <input type="checkbox" onChange={handleRemoteChange} checked={isRemote} />
        Remote
      </label>

      <label>
        <input type="checkbox" onChange={handleHybridChange} checked={isHybrid} />
        Hybrid
      </label>

      <OfferList offers={offers}/>
    </div>
  );
};