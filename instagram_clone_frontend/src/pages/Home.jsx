import React, { useEffect, useState } from "react";
import api from "../api/api";
import Navbar from "../components/Navbar";
import PostCard from "../components/PostCard";

export default function Home() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    api.get("/feed").then((res) => setPosts(res.data));
  }, []);

  return (
    <>
      <Navbar />
      <div className="max-w-md mx-auto mt-4">
        {posts.map((p) => (
          <PostCard key={p._id} post={p} />
        ))}
      </div>
    </>
  );
}
