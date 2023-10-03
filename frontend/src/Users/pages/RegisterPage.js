import React from "react";
import RegisterForm from "../components/RegisterForm";
import "../styles/RegisterPage.css";


const RegisterPage = () => {
  return (
    <div className="register-page">
      <h1>Register</h1>
      <RegisterForm className="register-form" />
    </div>
  );
};

export default RegisterPage;