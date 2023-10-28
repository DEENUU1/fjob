import React from 'react';

export const RemoteHybridOffer = ({ offer }) => {
  return (
    <div className="offer-remote-hybrid">
      {offer.is_remote && <span>Remote </span>}
      {offer.is_hybrid && <span>Hybrid </span>}
    </div>
  );
};
