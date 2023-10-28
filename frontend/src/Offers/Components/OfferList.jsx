import React from "react";
import "../Styles/OfferList.css";
import {OfferExperience} from "./Experience.jsx";
import {RemoteHybridOffer} from "./RemoteHybrid.jsx";


export const OfferList = ({ offers }) => {
  return (
    <ul>
      {offers.map((offer) => (
          <a className="offer" href={offer.url}>
            <div className="card-container">
              <div className="card-header">
                <h2>{offer.title}</h2>

                <OfferExperience offer={offer} />
                <RemoteHybridOffer offer={offer} />
              </div>

              <div className="card-description">
                <p>{offer.description.substring(0, 100) + "..."}</p>
              </div>

              <div className="card-additional">
              <div className="offer-skills">
                {offer.skills ? (
                  <ul>
                    {offer.skills.split(',').map((skill, index) => (
                      <li key={index} style={{ border: '1px solid black', display: 'inline-block' }}>{skill}</li>
                    ))}
                  </ul>
                ) : (
                  <span></span>
                )}
              </div>


              <div className="offer-salary-container">
                {offer.salary ? (
                    <ul>
                      {offer.salary.map((salaryData) => {
                        return (
                            <li className="offer-salary">{salaryData.salary_from} - {salaryData.salary_to} {salaryData.currency} / {salaryData.salary_schedule}

                              <ul className="offer-work-schedule">
                                {salaryData.work_schedule.map((workSchedule) => {
                                  return (
                                      <li>{workSchedule.name}</li>
                                  );
                                })}
                              </ul>
                              <ul className="offer-contract-type">
                                {salaryData.contract_type.map((contractType) => {
                                  return (
                                      <li>{contractType.name}</li>
                                  );
                                  })}
                              </ul>
                            </li>
                        );
                      })}
                    </ul>

                ) : (
                    <span></span>
                )}
              </div>
              </div>

              <div className="offer-meta">
                <span className="date-scraped">{offer.date_scraped} </span>
                <span className="website-source"><a href={offer.website.url}>{offer.website.name}</a></span>
              </div>

            </div>
          </a>
      ))}
    </ul>
  );
};
