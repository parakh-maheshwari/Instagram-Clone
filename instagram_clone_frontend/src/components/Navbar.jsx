import React from "react";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  return (
    <div className="flex justify-between items-center px-6 py-3 border-b bg-white">
      <h1 className="text-xl font-bold">Instagram</h1>
      <div className="flex gap-4">
        <button onClick={() => navigate("/home")}>Home</button>
        <button onClick={() => navigate("/create")}>Create</button>
        <button onClick={() => navigate("/profile/me")}>Profile</button>
      </div>
    </div>
  );
}
