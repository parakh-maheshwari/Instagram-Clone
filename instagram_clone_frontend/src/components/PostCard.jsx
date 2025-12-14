import React from "react";
import { useNavigate } from "react-router-dom";

export default function PostCard({ post }) {
  const navigate = useNavigate();

  return (
    <div className="bg-white border mb-4">
      <img src={post.image_url} alt="" />
      <div className="p-3">
        <p>{post.caption}</p>
        <button className="text-sm text-blue-500" onClick={() => navigate(`/post/${post._id}`)}>
          View Post
        </button>
      </div>
    </div>
  );
}
