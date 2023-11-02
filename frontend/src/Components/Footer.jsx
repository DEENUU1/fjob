import React from "react";
import "./footer.css";
import {useTranslation} from "react-i18next";

export const Footer = () => {
  const {t, i18n} = useTranslation();

  return (
    <footer className="page-footer font-small blue footer">
      <div className="footer-copyright text-center py-3">
          {t("footer.madeby")}
        <a
          href="https://github.com/DEENUU1"
          target="_blank"
          rel="noopener noreferrer"
          className="author"
        >
          {" "}
          Kacper Włodarczyk
        </a>
      </div>
    </footer>
  );
};
