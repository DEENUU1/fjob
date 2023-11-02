import React, { useState } from "react";
import axios from "axios";
import "../Styles/contactformpage.css";
import { Header } from "../Components/Header.jsx";
import { toast } from "react-toastify";
import {useTranslation} from "react-i18next";

export const ContactFormPage = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [content, setContent] = useState("");
  const {t, i18n} = useTranslation();

  const handleSubmit = async (event) => {

    event.preventDefault();

    try {
      const response = await axios.post(
        "http://localhost:8000/messages/send/",
        {
          name,
          email,
          content,
        },
      );

      if (response.status === 201) {
        toast.success("Message sent", {
          position: "top-center",
          autoClose: 5000,
          hideProgressBar: true,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "dark",
        });
      } else {
        toast.error("Failed to send message!", {
          position: "top-center",
          autoClose: 5000,
          hideProgressBar: true,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "dark",
        });
      }
    } catch (e) {
      toast.error("Error!", {
        position: "top-center",
        autoClose: 5000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };

  return (
    <div>
      <Header />
      <form className="contact-form" onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">{t("contact.name")}</label>
          <input
            type="text"
            id="name"
            name="name"
            className="required"
            value={name}
            onChange={(event) => setName(event.target.value)}
          />
        </div>
        <div>
          <label htmlFor="email">{t("contact.email")}</label>
          <input
            type="email"
            id="email"
            name="email"
            className="required"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </div>
        <div>
          <label htmlFor="message">{t("contact.message")}</label>
          <textarea
            id="message"
            name="message"
            value={content}
            onChange={(event) => setContent(event.target.value)}
          />
        </div>
        <div>
          <button type="submit">{t("contact.send")}</button>
        </div>
      </form>
    </div>
  );
};
