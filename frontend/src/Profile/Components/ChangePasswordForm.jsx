import React, { useState } from "react";
import "../Styles/passwordchangeform.css";
import { toast } from "react-toastify";
import {useTranslation} from "react-i18next";

export const ChangePasswordForm = ({ token }) => {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const {t, i18n} = useTranslation();

  const handleOldPasswordChange = (e) => {
    setOldPassword(e.target.value);
  };

  const handleNewPasswordChange = (e) => {
    setNewPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const endpoint = "http://localhost:8000/api/v1/users/change-password/";
    const headers = {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    };

    const data = {
      old_password: oldPassword,
      new_password: newPassword,
    };

    try {
      const response = await fetch(endpoint, {
        method: "PUT",
        headers: headers,
        body: JSON.stringify(data),
      });

      if (response.status === 200) {
        toast.success("Password has been changed", {
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
        toast.error("Invalid credential!", {
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
      <h2>Change password</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="oldPassword">{t("profile.oldpassword")}</label>
          <input
            type="password"
            id="oldPassword"
            value={oldPassword}
            onChange={handleOldPasswordChange}
            required
          />
        </div>
        <div>
          <label htmlFor="newPassword">{t("profile.newpassword")}</label>
          <input
            type="password"
            id="newPassword"
            value={newPassword}
            onChange={handleNewPasswordChange}
            required
          />
        </div>
        <button className="button-reset" type="submit">
          {t("profile.changepassword")}
        </button>
      </form>
    </div>
  );
};