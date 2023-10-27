import {useEffect, useState} from "react";
import axios from "axios";
import ErrorAlert from "../../Components/Alert.jsx";
import {useNavigate} from "react-router-dom";

export const Logout = () => {
    const [errorMessages, setErrorMessages] = useState([]);
    const navigate = useNavigate();


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
                navigate("/login");
            } catch (error) {
              console.error(error);

              if (error.response && error.response.data) {
                const errorData = error.response.data;
                const errorMessages = Object.values(errorData).flat();
                setErrorMessages(errorMessages);
              } else {
                setErrorMessages(["An error occurred."]);
              }
            }
        })();
    }, []);


    return (
        <div>
        {errorMessages.length > 0 && <ErrorAlert errors={errorMessages} />}
        </div>
    )
}