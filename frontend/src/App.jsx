import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {Login} from "./Authentication/Components/Login.jsx";
import {Navigation} from './Navigation.jsx';
import {Logout} from './Authentication/Components/Logout.jsx';
import {Register} from './Authentication/Components/Register.jsx';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";

function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            <Route path="/login" element={<Login/>}/>
            <Route path="/logout" element={<Logout/>}/>
            <Route path="/register" element={<Register/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;