import React from "react";
import "../styles/OfferCard.css";

const OfferCard = ({ offer }) => {
  return (
    <div className="offer-card">
      <h3>{offer.title}</h3>
      <p>Salary:</p> 
      <ul>
        {offer.salary.map((salary) => (
          <li key={salary.id}>
            {salary.salary_from} - {salary.salary_to} {salary.currency}
          </li>
        ))}
      </ul>
      {offer.location ? (
        <p>Location: {offer.city}, {offer.country}</p>
      ) : (
        <p className="empty">Location</p>
      )}
      {offer.remote ? (
        <p>Remote: Yes</p>
      ) : (
        <p>Remote: No</p>
      )}
      {offer.hybrid ? (
        <p>Hybrid: Yes</p>
      ) : (
        <p>Hybrid: No</p>
      )}
      {offer.experience_level ? (
        <p>Experience level: {offer.experience_level}</p>
      ) : (
        <p className="empty">Experience level</p>
      )}
      {offer.skills ? (
        <p>Skills: {offer.skills}</p>
      ) : (
        <p className="empty">Skills</p>
      )}
      {offer.company_name ? (
        <p>Company name: {offer.company_name}</p>
      ) : (
        <p className="empty">Company name</p>
      )}
      {offer.date_scraped ? (
        <p>Date scraped: {offer.date_scraped}</p>
      ) : (
        <p className="empty">Date scraped</p>
      )}
    </div>
  );
};

export default OfferCard;
