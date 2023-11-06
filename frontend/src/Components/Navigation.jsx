import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import React, { useState, useEffect } from "react";
import {useTranslation} from "react-i18next";
import Dropdown from "react-bootstrap/Dropdown";


const locales = {
    en: {title: "English"},
    pl: {title: "Polish"}
}


export function Navigation() {
  const [isAuth, setIsAuth] = useState(false);
  const {t, i18n} = useTranslation();

  useEffect(() => {
    if (localStorage.getItem("access_token") !== null) {
      setIsAuth(true);
    }
  }, [isAuth]);

  return (
    <div>
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
          <Navbar.Brand href="/">FJob</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">{t("nav.home")}</Nav.Link>
            <Nav.Link href="/contact">{t("nav.contact")}</Nav.Link>
          </Nav>
          <Nav>
            <Dropdown>
              <Dropdown.Toggle variant="dark" id="dropdown-lang">
                {t("nav.languages")}
              </Dropdown.Toggle>
              <Dropdown.Menu>
                {Object.keys(locales).map((locale) => (
                  <Dropdown.Item
                    key={locale}
                    onClick={() => i18n.changeLanguage(locale)}
                  >
                    {locales[locale].title}
                  </Dropdown.Item>
                ))}
              </Dropdown.Menu>
            </Dropdown>
            {isAuth ? (
              <Nav.Link href="/profile">
                {localStorage.getItem("username")}
              </Nav.Link>
            ) : null}
            {isAuth ? (
              <Nav.Link href="/logout">{t("nav.logout")}</Nav.Link>
            ) : (
              <Nav.Link href="/login">{t("nav.login")}</Nav.Link>
            )}
            {isAuth ? null : (
              <Nav.Link href="/register">{t("nav.register")}</Nav.Link>
            )}
          </Nav>
         </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
}
