import React from "react";
import {useTranslation} from "react-i18next";

export const RemoteHybridOffer = ({ offer }) => {
  const {t, i18n} = useTranslation();

  return (
    <div className="offer-remote-hybrid">
      {offer.is_remote && <span>{t("remote.remote")} </span>}
      {offer.is_hybrid && <span>{t("remote.hybrid")}</span>}
    </div>
  );
};
