import React, { useState } from "react";
import axios from "axios";

const OfferFilterForm = () => {
  const [query, setQuery] = useState("");
  const [country, setCountry] = useState("");
  const [city, setCity] = useState("");
  const [minSalary, setMinSalary] = useState("");
  const [maxSalary, setMaxSalary] = useState("");
  const [experienceLevel, setExperienceLevel] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await axios.get("http://localhost:8000/offers/", {
      params: {
        query,
        country,
        city,
        min_salary: minSalary,
        max_salary: maxSalary,
        experience_level: experienceLevel,
      },
    });
    
    const offers = response.data;

    offers.forEach((offers) => {
        console.log(offers);
    })

  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Wyszukaj ofertę"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
    <select value={country} onChange={(event) => setCountry(event.target.value)}>
        <option value="">Country</option>
        <option value="poland">Polska</option>
        <option value="germany">Niemcy</option>
        <option value="usa">USA</option>
      </select>
      <input
        type="text"
        placeholder="Miasto"
        value={city}
        onChange={(event) => setCity(event.target.value)}
      />
      <input
        type="number"
        placeholder="Minimalna pensja"
        value={minSalary}
        onChange={(event) => setMinSalary(event.target.value)}
      />
      <input
        type="number"
        placeholder="Maksymalna pensja"
        value={maxSalary}
        onChange={(event) => setMaxSalary(event.target.value)}
      />
      <select value={experienceLevel} onChange={(event) => setExperienceLevel(event.target.value)}>
        <option value="">Experience level</option>
        <option value="junior">Junior</option>
        <option value="mid">Mid</option>
        <option value="senior">Senior</option>
      </select>
      <button type="submit">Wyszukaj</button>
    </form>
  );
};

export default OfferFilterForm;