import {useEffect, useState} from "react";
import axios from "axios";

export const Logout = () => {

    useEffect(() => {
        (async () => {
            try {
                const Token = localStorage.getItem('access_token')
                const {data} = await axios.post('http://localhost:8000/users/logout/',
                    {refresh_token:localStorage.getItem('refresh_token')}
                    ,{headers: {'Content-Type': 'application/json','Authorization': `Bearer ${Token} `}},
                    {withCredentials: true});

                localStorage.clear();
                axios.defaults.headers.common['Authorization'] = null;
                window.location.href = '/login'
            } catch (e) {
                console.log('logout not working')
            }
        })();
    }, []);


    return (
        <div></div>
    )
}