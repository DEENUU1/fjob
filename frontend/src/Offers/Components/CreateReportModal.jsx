import React, { useState, useEffect } from "react";
import "../Styles/reportmodal.css";
import axios from "axios";
import { IoClose } from "react-icons/io5";
import { toast } from "react-toastify";
import {useTranslation} from "react-i18next";

export const CreateReport = ({ offerId, onClose }) => {
  const {t, i18n} = useTranslation();
  const [message, setMessage] = useState("");
  const token = localStorage.getItem("access_token");
  const userid = localStorage.getItem("user_id");
  const data = {
    message,
    offer: offerId,
    user: userid,
  };

  useEffect(() => {
    setMessage("");
  }, [offerId]);

  const handleSubmit = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/reports/",
        data,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      toast.success("Report sent", {
        position: "top-center",
        autoClose: 5000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
      onClose();
    } catch (error) {
      toast.error("Failed to send report!", {
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
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <div className="modal-header">
          <button type="button" className="close" onClick={onClose}>
            <IoClose />
          </button>
        </div>
        <div className="modal-body">
          <input
            type="text"
            className="form-control"
            placeholder={t("report.placeholder")}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>
        <div className="modal-footer">
          <button
            type="button"
            className="btn btn-primary"
            onClick={handleSubmit}
          >
            {t("report.send")}
          </button>
        </div>
      </div>
    </div>
  );
};
