import { Header } from "../Components/Header.jsx";
import { ChangePasswordForm } from "../Components/ChangePasswordForm.jsx";

export const UserChangePasswordPage = () => {
  const token = localStorage.getItem("access_token");

  return (
    <div>
      <ChangePasswordForm token={token} />
    </div>
  );
};
