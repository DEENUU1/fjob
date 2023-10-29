import {Header} from "../Components/Header.jsx";


const UserProfilePage = () => {
    const username = localStorage.get("username");


    return (
        <div>
            <Header username={username}/>
        </div>
    );
};

export default UserProfile;
