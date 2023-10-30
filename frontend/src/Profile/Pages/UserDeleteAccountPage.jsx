import { Header } from "../Components/Header.jsx";
import { AccountDeleteForm } from "../Components/AccountDeleteForm.jsx";

export const UserDeleteAccountPage = () => {
  const token = localStorage.getItem("access_token");

  return (
    <div>
      <AccountDeleteForm token={token} />
    </div>
  );
};
