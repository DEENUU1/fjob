import axios from "axios";
import {useState} from "react";
import "../Styles/LoginStyle.css";
import {useNavigate} from "react-router-dom";
import ErrorAlert from "./Alert.jsx";

export const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const navigate = useNavigate();
    const [errorMessages, setErrorMessages] = useState([]);

  const submit = async e => {
    e.preventDefault();

    const user = {
      username: username,
      email: email,
      password: password,
    };

    try {
      const { data } = await axios.post('http://localhost:8000/users/register/', user, {
        headers: {
          'Content-Type': 'application/json'
        },
        withCredentials: true
      });

      console.log(data);

      navigate('/login');
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
            <h3 className="Auth-form-title">Sign up</h3>
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
              <label>Email</label>
              <input
                className="form-control mt-1"
                placeholder="Enter Username"
                name='email'
                type='email'
                value={email}
                required
                onChange={e => setEmail(e.target.value)}
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