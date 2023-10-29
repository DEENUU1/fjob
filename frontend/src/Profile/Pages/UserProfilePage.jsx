import {Header} from "../Components/Header.jsx";
import {PasswordResetForm} from "../Components/PasswordResetForm.jsx";


export const UserProfilePage = () => {
    const username = localStorage.getItem("username");
    const token = localStorage.getItem("access_token");

    return (
        <div>
            <Header username={username}/>
            <PasswordResetForm token={token} />

        </div>
    );
};
