import React from "react";
import Navbar from "../components/Navbar";

export default function PostDetail() {
  return (
    <div>
      <Navbar />
      <div className="max-w-3xl mx-auto mt-10 flex gap-6">
        <img
          src="https://picsum.photos/400"
          className="w-1/2"
        />

        <div className="w-1/2">
          <p className="font-semibold mb-2">alice</p>
          <p>Nice photo!</p>

          <input
            placeholder="Add a comment..."
            className="border w-full p-2 mt-4"
          />
        </div>
      </div>
    </div>
  );
}
