import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {Login} from "./Authentication/Pages/Login.jsx";
import {Navigation} from './Components/Navigation.jsx';
import {Logout} from './Authentication/Components/Logout.jsx';
import {Register} from './Authentication/Pages/Register.jsx';
import {Home} from './Home/Pages/Home.jsx';
import {Footer} from './Components/Footer.jsx';
import {OffersListPage} from './Offers/Pages/OffersListPage.jsx';
import {ContactFormPage} from "./Contact/Pages/ContactFormPage.jsx"
import {UserProfilePage} from "./Profile/Pages/UserProfilePage.jsx";
import {UserChangePasswordPage} from "./Profile/Pages/UserChangePasswordPage.jsx";
import {UserDeleteAccountPage} from "./Profile/Pages/UserDeleteAccountPage.jsx";


function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            <Route path="/login" element={<Login/>}/>
            <Route path="/logout" element={<Logout/>}/>
            <Route path="/register" element={<Register/>}/>
            <Route path="/" element={<Home/>}/>
            <Route path="/offers" element={<OffersListPage/>}/>
            <Route path="/contact" element={<ContactFormPage/>}/>
            <Route path="/profile" element={<UserProfilePage/>}/>
            <Route path="/profile/delete" element={<UserDeleteAccountPage/>}/>
            <Route path="/profile/password_change" element={<UserChangePasswordPage/>} />
        </Routes>
    <Footer></Footer>
    </BrowserRouter>;
}

export default App;