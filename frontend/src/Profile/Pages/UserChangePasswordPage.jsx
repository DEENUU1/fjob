import {Header} from "../Components/Header.jsx";
import {ChangePasswordForm} from "../Components/PasswordResetForm.jsx";


export const UserChangePasswordPage = () => {
    const token = localStorage.getItem("access_token");

    return (
        <div>
            <Header username={username}/>
            <ChangePasswordForm token={token} />
        </div>
    );
};
