import React, { useState, useEffect } from "react";

export const Localization = ({ localizations }) => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    if (localizations.length > 1) {
      setCount(localizations.length - 1);
    }
  }, [localizations]);

  return (
    <div className="offer-location">
      {localizations.length > 0 && (
        <span>
          {localizations[0].country} {localizations[0].region} {localizations[0].city}
        </span>
      )}
      {count > 0 && <div>+ {count} locations</div>}
    </div>
  );
};
