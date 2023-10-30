import { useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

export const Logout = () => {
  const navigate = useNavigate();
  const Token = localStorage.getItem("access_token");

  useEffect(() => {
    (async () => {
      try {
        const { data } = await axios.post(
          "http://localhost:8000/users/logout/",
          { refresh_token: localStorage.getItem("refresh_token") },
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${Token} `,
            },
          },
          { withCredentials: true },
        );

        localStorage.clear();
        axios.defaults.headers.common["Authorization"] = null;
        navigate("/login");
      } catch (error) {
        console.error(error);

        if (error.response && error.response.data) {
          toast.error("Failed to logout!", {
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
          toast.error("Error!", {
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
      }
    })();
  }, []);

  return <div></div>;
};