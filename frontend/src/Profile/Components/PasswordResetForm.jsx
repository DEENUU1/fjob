import React, { useState } from 'react';

export const PasswordResetForm = ({token}) => {
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleOldPasswordChange = (e) => {
    setOldPassword(e.target.value);
  };

  const handleNewPasswordChange = (e) => {
    setNewPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Define the API endpoint and headers
    const endpoint = 'http://localhost:8000/users/change-password/';
    const headers = {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`, // Replace with your actual access tokenrer', // Replace with your actual access token
    };

    // Create a data object with old_password and new_password
    const data = {
      old_password: oldPassword,
      new_password: newPassword,
    };

    try {
      const response = await fetch(endpoint, {
        method: 'PUT',
        headers: headers,
        body: JSON.stringify(data),
      });

      if (response.status === 200) {
        setMessage('Password successfully changed.');
      } else {
        setMessage('Password change failed. Please check your old password.');
      }
    } catch (error) {
      setMessage('An error occurred while changing the password.');
    }
  };

  return (
    <div>
      <h2>Password Reset</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="oldPassword">Old Password</label>
          <input
            type="password"
            id="oldPassword"
            value={oldPassword}
            onChange={handleOldPasswordChange}
            required
          />
        </div>
        <div>
          <label htmlFor="newPassword">New Password</label>
          <input
            type="password"
            id="newPassword"
            value={newPassword}
            onChange={handleNewPasswordChange}
            required
          />
        </div>
        <button type="submit">Reset Password</button>
      </form>
      <p>{message}</p>
    </div>
  );
};