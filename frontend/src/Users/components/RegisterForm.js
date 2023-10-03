import React, { useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
import "../styles/RegisterForm.css";

const RegisterForm = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isRegistered, setIsRegistered] = useState(false);
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

try {
  const response = await axios.post("http://localhost:8000/users/register", {
    username,
    email,
    password,
  });

  if (response.status === 201) {
    setIsRegistered(true);
  } else if (response.status === 400) {
    // Check if response.data has errors
    if (response.data && response.data.errors) {
      setErrors(response.data.errors);
    } else {
      // Handle unexpected error
      setErrors(["An unexpected error occurred."]);
    }
  }
} catch (error) {
  setErrors(["An unexpected error occurred."]);
}}

  if (isRegistered) {
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
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="E-mail"
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

export default RegisterForm;