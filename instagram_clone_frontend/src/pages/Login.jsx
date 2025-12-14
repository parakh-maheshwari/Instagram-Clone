import React, { useState } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const login = async () => {
    const res = await api.post("/users/login", { email, password });
    localStorage.setItem("token", res.data.access_token);
    navigate("/home");
  };

  return (
    <div className="h-screen flex items-center justify-center">
      <div className="bg-white p-6 w-80 shadow">
        <h2 className="text-xl text-center mb-4">Login</h2>
        <input className="border p-2 w-full mb-2" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
        <input className="border p-2 w-full mb-4" type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
        <button onClick={login} className="bg-blue-500 text-white w-full py-2">Login</button>
      </div>
    </div>
  );
}
