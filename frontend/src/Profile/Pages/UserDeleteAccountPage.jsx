import {Header} from "../Components/Header.jsx";
import {AccountDeleteForm} from "../Components/AccountDeleteForm.jsx";


export const UserDeleteAccountPage = () => {
    const token = localStorage.getItem("access_token");

    return (
        <div>
            <Header username={username}/>
            <AccountDeleteForm token={token} />
        </div>
    );
};
