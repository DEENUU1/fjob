import axios from "axios";
import { useState } from "react";
import "../Styles/login.css";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import {useTranslation} from "react-i18next";

export const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const navigate = useNavigate();
  const {t, i18n} = useTranslation();
  const [termsAccepted , setTermsAccepted] = useState(false)




  const submit = async (e) => {
    e.preventDefault();

    if (!termsAccepted) {
      toast.info("Please accept the terms of service to register.", {
        position: "top-center",
        autoClose: 5000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
    })
  }

    const user = {
      username: username,
      email: email,
      password: password,
    };

    try {
      const { data } = await axios.post(
        "http://localhost:8000/api/v1/users/register/",
        user,
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        },
      );
      toast.success("Account has been created", {
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
    } catch (error) {
      console.error(error);

      if (error.response && error.response.data) {
        const errorData = error.response.data;
        const errorMessages = Object.values(errorData).flat();
        toast.error("Failed to sign up!", {
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
          <h3 className="Auth-form-title">{t('register.header')}</h3>

          <div className="form-group mt-3">
            <label>{t('register.labelusername')}</label>
            <input
              className="form-control mt-1"
              placeholder={t('register.placeholderusername')}
              name="username"
              type="text"
              value={username}
              required
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>

          <div className="form-group mt-3">
            <label>{t('register.labelemail')}</label>
            <input
              className="form-control mt-1"
              placeholder={t('register.placeholderemail')}
              name="email"
              type="email"
              value={email}
              required
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="form-group mt-3">
            <label>{t('register.labelpassword')}</label>
            <input
              name="password"
              type="password"
              className="form-control mt-1"
              placeholder={t('register.placeholderpassword')}
              value={password}
              required
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <div className="mt-1 d-flex align-items-center">
            <input
              type="checkbox"
              checked={termsAccepted}
              onChange={() => setTermsAccepted(!termsAccepted)}
              required
            />
            <label>{t('register.labelterms')}</label>

          </div>

          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary">
              {t('register.button')}
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};