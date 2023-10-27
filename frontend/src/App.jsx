import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {Login} from "./Authentication/Components/Login.jsx";
import {Navigation} from './Navigation.jsx';
import {Logout} from './Authentication/Components/Logout.jsx';

function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            <Route path="/login" element={<Login/>}/>
            <Route path="/logout" element={<Logout/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;