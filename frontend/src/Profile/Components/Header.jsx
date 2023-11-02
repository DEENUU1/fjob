import "../Styles/header.css";
import {useTranslation} from "react-i18next";

export const Header = ({ username }) => {
  const {t, i18n} = useTranslation();
  
  return (
    <header>
      <h1>{t("profile.header")} {username}</h1>
    </header>
  );
};