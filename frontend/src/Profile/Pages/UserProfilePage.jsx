import {Header} from "../Components/Header.jsx";
import Button from 'react-bootstrap/Button';
import "../Styles/profilepage.css";


export const UserProfilePage = () => {
    const username = localStorage.getItem("username");
    return (
        <div>
            <Header username={username}/>
            <div className="options">
            <Button className="button link-delete" href="/profile/delete" variant="link">Delete Account</Button>
            <Button className="button link-update" href="/profile/password_change" variant="link">Change Password</Button>
            </div>
        </div>
    );
};
