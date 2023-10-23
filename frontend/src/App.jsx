import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {Login} from "./Login";
// import {Home} from "./Home";
import {Navigation} from './Navigation';
import {Logout} from './Logout';

function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            {/*<Route path="/" element={<Home/>}/>*/}
            <Route path="/login" element={<Login/>}/>
            <Route path="/logout" element={<Logout/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;