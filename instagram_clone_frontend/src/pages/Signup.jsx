import React, { useState } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

export default function Signup() {
  const [form, setForm] = useState({});
  const navigate = useNavigate();

  const signup = async () => {
    await api.post("/users/signup", form);
    navigate("/");
  };

  return (
    <div className="h-screen flex justify-center items-center">
      <div className="bg-white p-6 w-80 shadow">
        <h2 className="text-xl mb-4 text-center">Signup</h2>
        <input className="border p-2 w-full mb-2" placeholder="Username" onChange={(e) => setForm({ ...form, username: e.target.value })} />
        <input className="border p-2 w-full mb-2" placeholder="Email" onChange={(e) => setForm({ ...form, email: e.target.value })} />
        <input className="border p-2 w-full mb-4" type="password" placeholder="Password" onChange={(e) => setForm({ ...form, password: e.target.value })} />
        <button onClick={signup} className="bg-blue-500 text-white w-full py-2">Signup</button>
      </div>
    </div>
  );
}
