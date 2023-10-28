import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import React, {useState, useEffect} from 'react';

export function Navigation() {
    const [isAuth, setIsAuth] = useState(false);
    useEffect(() => {
        if (localStorage.getItem('access_token') !== null) {
            setIsAuth(true);
        }
    }, [isAuth]);

    return (
        <div>
            <Navbar bg="light" variant="light">
                <Navbar.Brand href="/">FJob</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="/">Home</Nav.Link>
                    <Nav.Link href="/contact">Contact</Nav.Link>
                </Nav>
                <Nav>
                    {isAuth ? <Nav.Link href="/logout">Logout</Nav.Link> :
                        <Nav.Link href="/login">Login</Nav.Link>
                    }
                    {isAuth ?  null :
                        <Nav.Link href="/register">Register</Nav.Link>
                    }
                </Nav>
            </Navbar>
        </div>
    );
}
