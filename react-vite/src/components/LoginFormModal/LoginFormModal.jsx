import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  const demoUser = {
    email: "demo@aa.io",
    password: "password"
  };

  const handleDemoLogin = (e) => {
    e.preventDefault();

    dispatch(thunkLogin(demoUser))
      .then(() => {
        closeModal();
      })
      .catch((error) => {
        console.error("Login failed", error);
      });
  }

  return (
    <div className="login-form-container">
      <h1>Log In</h1>
      <form className="login-form" onSubmit={handleSubmit}>
        <label className="login-email">
          <input
            placeholder="Email"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p className="error-message">{errors.email}</p>}
        <label className="login-password">
          <input
            placeholder="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p className="error-message">{errors.password}</p>}
        <button type="submit">Log In</button>
      </form>
      <hr className="line"/>
      <button onClick={handleDemoLogin}>Log in as Demo User</button>
    </div>
  );
}

export default LoginFormModal;
