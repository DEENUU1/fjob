import {Header} from "../Components/Header.jsx";


export const UserProfilePage = () => {
    const username = localStorage.getItem("username");


    return (
        <div>
            <Header username={username}/>
        </div>
    );
};
