import React, { useState } from "react";
import axios from "axios";
import "../styles/OfferFilterForm.css";


const OfferFilterForm = ({onSubmit}) => {
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
    onSubmit(response.data);

  };

  return (
    <form onSubmit={handleSubmit} className="offer-filter-form">
      <input
        type="text"
        placeholder="Search phrase"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
        className="input-field"
      />
      <select
        value={country}
        onChange={(event) => setCountry(event.target.value)}
        className="select-field"
      >
        <option value="">Country</option>
        <option value="poland">Poland</option>
        <option value="germany">Germany</option>
      </select>
      <input
        type="text"
        placeholder="City"
        value={city}
        onChange={(event) => setCity(event.target.value)}
        className="input-field"
      />
      <input
        type="number"
        placeholder="Min Salary"
        value={minSalary}
        onChange={(event) => setMinSalary(event.target.value)}
        className="input-field"
      />
      <input
        type="number"
        placeholder="Max Salary"
        value={maxSalary}
        onChange={(event) => setMaxSalary(event.target.value)}
        className="input-field"
      />
      <select
        value={experienceLevel}
        onChange={(event) => setExperienceLevel(event.target.value)}
        className="select-field"
      >
        <option value="">Experience level</option>
        <option value="intern">Intern</option>
        <option value="junior">Junior</option>
        <option value="mid">Mid</option>
        <option value="senior">Senior</option>
      </select>
      <button type="submit" className="submit-button">
        Search
      </button>
    </form>

  );
};  

export default OfferFilterForm;
