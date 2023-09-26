import React, { useState } from "react";

const OfferList = () => {
  const [offers, setOffers] = useState([]);

  useEffect(() => {
    const fetchOffers = async () => {
      const response = await axios.get("/api/offers/");
      setOffers(response.data);
    };

    fetchOffers();
  }, []);

  return (
    <ul>
      {offers.map((offer) => (
        <li key={offer.id}>{offer.title}</li>
      ))}
    </ul>
  );
};

export default OfferList;
