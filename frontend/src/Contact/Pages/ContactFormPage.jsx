import React, { useState } from "react";
import axios from "axios";
import "../Styles/contactformpage.css";
import {Header} from "../Components/Header.jsx";
import {toast} from "react-toastify";

export const ContactFormPage = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [content, setContent] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post(
        "http://localhost:8000/messages/send/",
        {
          name,
          email,
          content,
        },
      );

      if (response.status === 201) {
        toast.success('Message sent', {
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
        toast.error('Failed to send message!', {
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
    } catch (e) {
      toast.error('Error!', {
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
    <div>
        <Header />
        <form className="contact-form" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="name">Name</label>
            <input type="text" id="name" name="name" className="required" value={name} onChange={(event) => setName(event.target.value)} />
          </div>
          <div>
            <label htmlFor="email">Email</label>
            <input type="email" id="email" name="email" className="required" value={email} onChange={(event) => setEmail(event.target.value)} />
          </div>
          <div>
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              name="message"
              value={content}
              onChange={(event) => setContent(event.target.value)}
            />
          </div>
          <div>
            <button type="submit">Send Message</button>
          </div>
        </form>
    </div>
  );
};
