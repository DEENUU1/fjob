import React from "react";
import LoginForm from "../components/LoginForm";
import "../styles/RegisterPage.css";


const LoginPage = () => {
  return (
    <div className="register-page">
      <h1>Login</h1>
      <LoginForm className="register-form" />
    </div>
  );
};

export default LoginPage;