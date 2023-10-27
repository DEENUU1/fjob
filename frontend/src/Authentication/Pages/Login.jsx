import axios from "axios";
import {useState} from "react";
import "../../../public/css/login.css";
import ErrorAlert from "../../Components/Alert.jsx";

export const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessages, setErrorMessages] = useState([]);

    const submit = async e => {
        e.preventDefault();

        const user = {
            username: username,
            password: password
          };
        try {
            const {data} = await axios.post('http://localhost:8000/token/', user,
                {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                },
                {
                    withCredentials: true
                });

            console.log(data)
            localStorage.clear();
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            axios.defaults.headers.common['Authorization'] = `Bearer ${data['access']}`;
            window.location.href = '/'
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
    }

    return(
        <div className="Auth-form-container">
        {errorMessages.length > 0 && <ErrorAlert errors={errorMessages} />}
        <form className="Auth-form" onSubmit={submit}>
          <div className="Auth-form-content">
            <h3 className="Auth-form-title">Sign In</h3>
            <div className="form-group mt-3">
              <label>Username</label>
              <input
                className="form-control mt-1"
                placeholder="Enter Username"
                name='username'
                type='text'
                value={username}
                required
                onChange={e => setUsername(e.target.value)}
              />
            </div>
            <div className="form-group mt-3">
              <label>Password</label>
              <input
                name='password'
                type="password"
                className="form-control mt-1"
                placeholder="Enter password"
                value={password}
                required
                onChange={e => setPassword(e.target.value)}
              />
            </div>
            <div className="d-grid gap-2 mt-3">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
          </div>
        </form>
    </div>

    )
}