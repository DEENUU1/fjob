import React, { useState } from "react";
import "../Styles/passwordchangeform.css";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import {useTranslation} from "react-i18next";

export const AccountDeleteForm = ({ token }) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const {t, i18n} = useTranslation();

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const endpoint = "http://localhost:8000/users/account-delete/";
    const headers = {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    };

    const data = {
      password: password,
      email: email,
      username: username,
    };

    try {
      const response = await fetch(endpoint, {
        method: "DELETE",
        headers: headers,
        body: JSON.stringify(data),
      });

      if (response.status === 204) {
        localStorage.clear();
        toast.success("Your account has been deleted", {
          position: "top-center",
          autoClose: 5000,
          hideProgressBar: true,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "dark",
        });
        navigate("/login");
      } else {
        toast.error("Invalid credentials!", {
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
    } catch (error) {
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
    <div className="form-container">
      <h2>Delete account</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">{t("profile.email")}</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={handleEmailChange}
            required
          />
        </div>
        <div>
          <label htmlFor="username">{t("profile.username")}</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={handleUsernameChange}
            required
          />
        </div>
        <div>
          <label htmlFor="password">{t("profile.password")}</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={handlePasswordChange}
            required
          />
        </div>
        <button className="button-delete" type="submit">
          {t("profile.delete")}
        </button>
      </form>
    </div>
  );
};