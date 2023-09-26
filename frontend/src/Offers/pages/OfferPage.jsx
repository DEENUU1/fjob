import React, { useState, useEffect } from "react";
import OfferFilterForm from "./components/OfferFilterForm";
import OfferList from "./components/OfferList";

const App = () => {
  const [offers, setOffers] = useState([]);

  useEffect(() => {
    const fetchOffers = async () => {
      const response = await axios.get("/api/offers/");
      setOffers(response.data);
    };

    fetchOffers();
  }, []);

  return (
    <div>
      <OfferFilterForm offers={offers} setOffers={setOffers} />
      <OfferList offers={offers} />
    </div>
  );
};

export default App;
