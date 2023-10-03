import React, { useState, useHistory } from "react";
import { Button } from "antd";

const LogoutButton = () => {
  const [isLoggingOut, setIsLoggingOut] = useState(false);
  const history = useHistory();

  const logout = async () => {
    setIsLoggingOut(true);
    try {
      await fetch("http://localhost:8000/users/logout", {
        method: "POST",
      });
      history.push("/login");
    } catch (error) {
      setIsLoggingOut(false);
      console.error(error);
    }
  };

  return (
    <Button type="primary" onClick={logout} disabled={isLoggingOut}>
      Logout
    </Button>
  );
};

export default LogoutButton;
