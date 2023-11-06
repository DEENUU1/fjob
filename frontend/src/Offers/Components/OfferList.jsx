import React, {useEffect, useState} from "react";
import "../Styles/offerlist.css";
import { RemoteHybridOffer } from "./RemoteHybrid.jsx";
import { Localization } from "./Localization.jsx";
import { CreateReport } from "./CreateReportModal.jsx";
import {useTranslation} from "react-i18next";
import {SalaryDetails} from "./SalaryDetails.jsx";
import Button from "react-bootstrap/Button";
import {Converter} from "./DateConverter.jsx";

export const OfferList = ({ offers }) => {
  const [showModal, setShowModal] = useState(false);
  const {t, i18n} = useTranslation();

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
              <h5>
                <a className="offer-url" href={offer.url}>
                  {offer.title}
                </a>
              </h5>

              <Button variant="danger" className="report-button" size="sm" onClick={handleShowModal}>{t("offer.report")}</Button>
              {showModal && (
                <CreateReport offerId={offer.id} onClose={handleCloseModal} />
              )}

              <RemoteHybridOffer offer={offer} />
            </div>

            <div className="card-additional">
              <div className="offer-skills">
                <ul style={{ display: "flex", flexWrap: "wrap" }}>
                  {offer.experience_level && offer.experience_level.length > 0 ? (
                    offer.experience_level.map((experienceLevel) => (
                      <li key={experienceLevel.id} style={{ marginRight: 10 }}>
                        <span className="skills">{experienceLevel.name}</span>
                      </li>
                    ))
                  ) : null}

                  {offer.skills ? (
                    offer.skills.split(",").map((skill, index) => (
                      <li key={index} style={{ marginRight: 10 }}>
                        <span className="skills">{skill}</span>
                      </li>
                    ))
                  ) : null}
                </ul>
              </div>

              <div className="card-description">
                {offer.description ? (
                  <p>
                    {offer.description.substring(0, 200) +
                      (offer.description.length > 200 ? "..." : "")}
                  </p>
                ) : (
                  <p></p>
                )}
              </div>
            </div>
              {offer.salary.map((salary, index) => (
                <SalaryDetails key={index} salaryData={salary} />
              ))}
            <div className="card-footer">
              <Localization localizations={offer.localizations} />
              <div className="offer-meta">
                <span className="date-scraped">
                  <Converter date={offer.date_scraped} />
                </span>

                <span className="website-source">
                  {offer.website && <a href={offer.website.url}>{offer.website.name}</a>}

                </span>
              </div>
            </div>
          </div>
        </div>
      ))}
    </ul>
  );
};
