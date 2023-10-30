import React, { useState, useEffect } from "react";
import "../Styles/reportmodal.css";
import axios from "axios";
import {IoClose} from "react-icons/io5";


export const CreateReport = ({ offerId, onClose }) => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    setMessage("");
  }, [offerId]);

  const handleSubmit = async () => {
    const token = localStorage.getItem("access_token");
    const data = {
      message,
      offer: offerId,
      user: 1,
    };

    try {
      const response = await axios.post("http://localhost:8000/reports/", data, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      console.log("Report sent");
      // Close the modal after the report is sent
      onClose();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <div className="modal-header">
          <h2 className="modal-title">Report offer</h2>
          <button type="button" className="close" onClick={onClose}>
            <IoClose />
          </button>
        </div>
        <div className="modal-body">
          <input
            type="text"
            className="form-control"
            placeholder="Tell us what is wrong with this offer"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>
        <div className="modal-footer">
          <button type="button" className="btn btn-primary" onClick={handleSubmit}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
};
