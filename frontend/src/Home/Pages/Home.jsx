import React from "react";
import "../Styles/home.css";
import { useTranslation} from "react-i18next";

export const Home = () => {
  const {t, i18n} = useTranslation();

  return (
    <div>
      <div className="container content">
        <div className="row">
          <div className="col-sm-3 talk">
            <h1>FJob</h1>
            <h3>{t("home.title")}</h3>
            {/*Find job quicker*/}
            <br />
            <h6 className="bold-four">
              {t("home.subtitle")}
            </h6>
            {/*FJob collects data on job offers from many websites to help you find the best offer easily and quickly.*/}
            <br />
            <h6>
              <a className="btn btn-dark start start-two" href="/offers">
                {t("home.button")}
              </a>
              {/*Get Started*/}
            </h6>
          </div>
          <div className="col-sm-9 showcase-img">
            <img
              src="../../../public/images/reading-woman.png "
              alt="Reading Woman"
              className="img-fluid"
            />
          </div>
        </div>
      </div>

      <section className="features-icons bg-light text-center det-ails">
        <div className="container">
          <div className="row">
            <div className="col-lg-4">
              <div className="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
                <div className="features-icons-icon d-flex  icon-bra-ails">
                  <i className="icon-screen-desktop m-auto text-primary icon-ails"></i>
                </div>
                <h5>{t("home.features.title")}</h5>
                {/*Job offer scrapers*/}
                <p className="lead mb-0">
                  {t("home.features.subtitle")}
                </p>
                {/*Every day many scrapers collects and process data from many*/}
                {/*  websites!*/}
              </div>
            </div>
            <div className="col-lg-4">
              <div className="features-icons-item mx-auto mb-5 mb-lg-0 mb-lg-3">
                <div className="features-icons-icon d-flex  icon-bra-ails">
                  <i className="icon-layers m-auto text-primary icon-ails"></i>
                </div>
                <h5>{t("home.features.title2")}</h5>
                {/*Offers from companies*/}
                <p className="lead mb-0">
                  {t("home.features.subtitle2")}
                </p>
                {/*Companies can post job offers here for free!*/}
              </div>
            </div>
            <div className="col-lg-4">
              <div className="features-icons-item mx-auto mb-0 mb-lg-3">
                <div className="features-icons-icon d-flex  icon-bra-ails">
                  <i className="icon-check m-auto text-primary icon-ails"></i>
                </div>
                <h5>{t("home.features.title3")}</h5>
                {/*Notifications*/}
                <p className="lead mb-0">
                  {t("home.features.subtitle3")}
                </p>
                {/*Sign up to get emails about new job offers every day!*/}
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};