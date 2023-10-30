import "../Styles/header.css";

export const Header = ({ username }) => {
  return (
    <header>
      <h1>Welcome {username}</h1>
    </header>
  );
};