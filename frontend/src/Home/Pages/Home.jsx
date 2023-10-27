import React, { useState, useEffect } from "react";
import { Header } from "../Components/Header.jsx";
import { Features } from "../Components/Features.jsx";
import { About } from "../Components/About.jsx";
import { Services } from "../Components/Services.jsx";
import SmoothScroll from "smooth-scroll";
import "../Styles/HomeStyle.css";
import "../Styles/Styles.css";
import JsonData from "../data.json";

export const scroll = new SmoothScroll('a[href*="#"]', {
  speed: 1000,
  speedAsDuration: true,
});

export const Home = () => {
  const [landingPageData, setLandingPageData] = useState({});
  useEffect(() => {
    setLandingPageData(JsonData);
  }, []);

  return (
    <div>
      <Header data={landingPageData.Header} />
      <Features data={landingPageData.Features} />
      <About data={landingPageData.About} />
      <Services data={landingPageData.Services} />
    </div>
  );
};
