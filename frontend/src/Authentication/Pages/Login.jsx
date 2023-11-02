import axios from "axios";
import { useState } from "react";
import "../Styles/login.css";
import { toast } from "react-toastify";
import {useTranslation} from "react-i18next";

export const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const user = {
    username: username,
    password: password,
  };
  const {t, i18n} = useTranslation();

  const submit = async (e) => {
    e.preventDefault();

    try {
      const { data } = await axios.post(
        "http://localhost:8000/token/",
        user,
        {
          headers: {
            "Content-Type": "application/json",
          },
        },
        {
          withCredentials: true,
        },
      );

      localStorage.clear();
      localStorage.setItem("access_token", data.access);
      localStorage.setItem("refresh_token", data.refresh);
      localStorage.setItem("username", data.username);
      localStorage.setItem("user_id", data.user_id);
      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${data["access"]}`;
      toast.success("Successfully logged in", {
        position: "top-center",
        autoClose: 5000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
      window.location.href = "/";
    } catch (error) {
      console.error(error);

      if (error.response && error.response.data) {
        const errorData = error.response.data;
        const errorMessages = Object.values(errorData).flat();
        toast.error("Failed to log in!", {
          position: "top-center",
          autoClose: 5000,
          hideProgressBar: true,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
          theme: "dark",
        });
        toast.error(errorMessages, {
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
    }
  };

  return (
    <div className="Auth-form-container">
      <form className="Auth-form" onSubmit={submit}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">{t("login.header")}</h3>
          <div className="form-group mt-3">
            <label>{t("login.labelusername")}</label>
            <input
              className="form-control mt-1"
              placeholder={t("login.placeholderusername")}
              name="username"
              type="text"
              value={username}
              required
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="form-group mt-3">
            <label>{t("login.labelpassword")}</label>
            <input
              name="password"
              type="password"
              className="form-control mt-1"
              placeholder={t("login.placeholderpassword")}
              value={password}
              required
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary">
              {t("login.button")}
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};