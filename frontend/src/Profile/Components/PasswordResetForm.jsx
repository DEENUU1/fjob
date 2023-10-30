import React, { useState } from 'react';
import "../Styles/passwordchangeform.css";


export const ChangePasswordForm = ({token}) => {
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

    const endpoint = 'http://localhost:8000/users/change-password';
    const headers = {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
    };

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
    <div className="form-container">
      <h2>Change password</h2>
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
        <button className="button-reset" type="submit">Reset Password</button>
      </form>
      <strong>{message}</strong>
    </div>
  );
};