import { NavLink } from "react-router-dom";
import stackedLogo from "../../../public/Stacked-logo.png";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <nav className="nav-bar">
      <NavLink to="/" className="nav-link">
        <img src={stackedLogo} alt="Stacked Logo" className="home-logo" />
        <span className="home-link">STACKED</span>
      </NavLink>
      <ProfileButton />
    </nav>
  );
}

export default Navigation;
