import React, { useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
import "../styles/RegisterForm.css";

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLogin, setIsLogin] = useState(false);
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

try {
  const response = await axios.post("http://localhost:8000/users/login", {
    username,
    password,
  });

  if (response.status === 200) {
    setIsLogin(true);
  } else if (response.status === 400) {
    if (response.data && response.data.errors) {
      setErrors(response.data.errors);
    } else {
      setErrors(["An unexpected error occurred."]);
    }
  }
} catch (error) {
  setErrors(["An unexpected error occurred."]);
}}

  if (isLogin) {
    return <Navigate to="/" />;
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Submit</button>

      {errors.length > 0 && (
        <ul className="errors">
          {errors.map((error, index) => (
            <li key={index}>{error}</li>
          ))}
        </ul>
      )}
    </form>
  );
};

export default LoginForm;