import React, { useEffect, useState } from "react";
import axios from "axios";
import { OfferList } from "../Components/OfferList.jsx";
import "../Styles/filtersearch.css";
import { toast } from "react-toastify";
import {useTranslation} from "react-i18next";
import Container from "react-bootstrap/Container";


export const OffersListPage = () => {
  const [offers, setOffers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [sortOption, setSortOption] = useState("");
  const [query, setQuery] = useState("");
  const token = localStorage.getItem("access_token");
  const sortUrl = sortOption ? `&ordering=${sortOption}` : "";
  const queryUrl = query ? `&search=${query}` : "";
  const {t, i18n} = useTranslation();

  const loadOffers = () => {
    setIsLoading(true);

    axios
      .get(`http://localhost:8000/api/v1/offers/?${sortUrl}${queryUrl}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        setOffers(response.data.results);
        setIsLoading(false);
      })
      .catch((e) => {
        toast.error("Failed to load job offers!", {
          position: "top-center",
          autoClose: 5000,
          hideProgressBar: true,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "dark",
        });
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
    setQuery(e.currentTarget.elements.query.value);
  };

  return (
    <div>
      <div className="filter-search">
        <div className="search-container">
          <form className="search-form" onSubmit={handleSubmit}>
            <input
              id="query"
              type="text"
              name="query"
              placeholder={t("offer.searchplaceholder")}
            />
            <button type="submit">{t("offer.searchbutton")}</button>
          </form>
        </div>
        <div className="sort-container">
          <select
            value={sortOption}
            onChange={(e) => setSortOption(e.target.value)}
          >
            <option value="">{t("offer.sortby")}</option>
            <option value="-date_scraped">{t("offer.newest")}</option>
            <option value="date_scraped">{t("offer.oldest")}</option>
            <option value="-salary__salary_from">{t("offer.highest")}</option>
            <option value="salary__salary_from">{t("offer.lowest")}</option>
          </select>
        </div>
      </div>
      <Container>
        <OfferList offers={offers} />
      </Container>
    </div>
  );
};
