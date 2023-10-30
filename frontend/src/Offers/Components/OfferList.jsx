import React, { useState } from "react";
import "../Styles/offerlist.css";
import { OfferExperience } from "./Experience.jsx";
import { RemoteHybridOffer } from "./RemoteHybrid.jsx";
import { Localization } from "./Localization.jsx";
import { CreateReport } from "./CreateReportModal.jsx";

export const OfferList = ({ offers }) => {
  const [showModal, setShowModal] = useState(false);

  const handleShowModal = () => {
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  return (
    <ul>
      {offers.map((offer) => (
        <div className="offer">
          <div className="card-container">
            <div className="card-header">
              <h2>
                <a className="offer-url" href={offer.url}>
                  {offer.title}
                </a>
              </h2>

              <button onClick={handleShowModal}>Report</button>
              {showModal && (
                <CreateReport offerId={offer.id} onClose={handleCloseModal} />
              )}

              <OfferExperience offer={offer} />
              <RemoteHybridOffer offer={offer} />
            </div>

            <div className="card-additional">
              <div className="offer-skills">
                {offer.skills ? (
                  <span>
                    {offer.skills.split(",").map((skill, index) => (
                      <span className="skills" key={index}>
                        {skill}
                      </span>
                    ))}
                  </span>
                ) : (
                  <span></span>
                )}
              </div>

              <div className="card-description">
                <p>{offer.description.substring(0, 200) + "..."}</p>
              </div>

              <div className="offer-salary-container">
                {offer.salary ? (
                  <ul>
                    {offer.salary.map((salaryData) => {
                      return (
                        <li className="offer-salary">
                          {salaryData.salary_from} - {salaryData.salary_to}{" "}
                          {salaryData.currency} / {salaryData.salary_schedule}
                          <ul className="offer-work-schedule">
                            {salaryData.work_schedule.map((workSchedule) => {
                              return <li>{workSchedule.name}</li>;
                            })}
                          </ul>
                          <ul className="offer-contract-type">
                            {salaryData.contract_type.map((contractType) => {
                              return <li>{contractType.name}</li>;
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

            <div className="card-footer">
              <Localization localizations={offer.localizations} />
              <div className="offer-meta">
                <span className="date-scraped">{offer.date_scraped} </span>
                <span className="website-source">
                  <a href={offer.website.url}>{offer.website.name}</a>
                </span>
              </div>
            </div>
          </div>
        </div>
      ))}
    </ul>
  );
};
