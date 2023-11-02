import "../Styles/header.css";
import {useTranslation} from "react-i18next";

export const Header = () => {
  const {t, i18n} = useTranslation();


  return (
    <div className="header">
      <h1>{t("contact.header")}</h1>
        {/*Contact us*/}
    </div>
  );
};