import React, { useState } from "react";
import api from "../api/api";
import Navbar from "../components/Navbar";
import { useNavigate } from "react-router-dom";

export default function CreatePost() {
  const [image_url, setImage] = useState("");
  const [caption, setCaption] = useState("");
  const navigate = useNavigate();

  const submit = async () => {
    await api.post("/posts/", { image_url, caption });
    navigate("/home");
  };

  return (
    <>
      <Navbar />
      <div className="max-w-md mx-auto mt-6">
        <input className="border p-2 w-full mb-2" placeholder="Image URL" onChange={(e) => setImage(e.target.value)} />
        <input className="border p-2 w-full mb-4" placeholder="Caption" onChange={(e) => setCaption(e.target.value)} />
        <button onClick={submit} className="bg-blue-500 text-white w-full py-2">Post</button>
      </div>
    </>
  );
}
