import { useState } from 'react';
import Alert from 'react-bootstrap/Alert';
import "../../public/css/alert.css";

function ErrorAlert({ errors }) {
  const [show, setShow] = useState(true);

  if (show) {
    return (
      <Alert variant="danger" onClose={() => setShow(false)} dismissible>
        <Alert.Heading>Error!</Alert.Heading>
        <ul>
          {errors.map((error, index) => (
            <li key={index}>{error}</li>
          ))}
        </ul>
      </Alert>
    );
  }

  return null;
}

export default ErrorAlert;