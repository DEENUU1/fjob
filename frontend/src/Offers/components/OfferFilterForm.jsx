import React, { useState, useEffect } from "react";

const OfferFilterForm = () => {
  const [query, setQuery] = useState("");
  const [country, setCountry] = useState("");
  const [city, setCity] = useState("");
  const [minSalary, setMinSalary] = useState("");
  const [maxSalary, setMaxSalary] = useState("");
  const [experienceLevel, setExperienceLevel] = useState("");

  const [offers, setOffers] = useState([]);

  useEffect(() => {
    const fetchOffers = async () => {
      const response = await axios.get(
        `/api/offers/?query=${query}&country=${country}&city=${city}&min_salary=${minSalary}&max_salary=${maxSalary}&experience_level=${experienceLevel}`
      );
      setOffers(response.data);
    };

    fetchOffers();
  }, [query, country, city, minSalary, maxSalary, experienceLevel]);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await axios.get(
      `/api/offers/?query=${query}&country=${country}&city=${city}&min_salary=${minSalary}&max_salary=${maxSalary}&experience_level=${experienceLevel}`
    );
    setOffers(response.data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Query"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      <input
        type="text"
        placeholder="Country"
        value={country}
        onChange={(event) => setCountry(event.target.value)}
      />
      <input
        type="text"
        placeholder="City"
        value={city}
        onChange={(event) => setCity(event.target.value)}
      />
      <input
        type="number"
        placeholder="Min salary"
        value={minSalary}
        onChange={(event) => setMinSalary(event.target.value)}
      />
      <input
        type="number"
        placeholder="Max salary"
        value={maxSalary}
        onChange={(event) => setMaxSalary(event.target.value)}
      />
      <select value={experienceLevel} onChange={(event) => setExperienceLevel(event.target.value)}>
        <option value="">Select experience level</option>
        <option value="entry">Entry level</option>
        <option value="mid">Mid level</option>
        <option value="senior">Senior level</option>
      </select>
      <button type="submit">Submit</button>
    </form>
  );
};

export default OfferFilterForm;