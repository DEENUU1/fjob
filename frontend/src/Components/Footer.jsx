import React from "react";
import "./footer.css";

export const Footer = () => {
  return (
    <footer className="page-footer font-small blue footer">
      <div className="footer-copyright text-center py-3">
        Made by
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
