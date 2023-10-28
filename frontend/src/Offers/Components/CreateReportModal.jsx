import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import "../Styles/ReportModal.css";
import axios from "axios";

export const CreateReport = ({ offerId }) => {
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
    const response = await axios.post(
      "http://localhost:8000/reports/",
      data,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    console.log("Message sent successfully!");
  } catch (error) {
    console.error(error);
  }
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <div className="modal-header">
          <h2>Tell us what is wrong with this job offer.</h2>
          <button type="button" className="close" data-dismiss="modal">
            &times;
          </button>
        </div>
        <div className="modal-body">
          <input
            type="text"
            className="form-control"
            placeholder="Wprowadź wiadomość"
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