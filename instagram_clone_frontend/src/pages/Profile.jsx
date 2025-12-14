import React from "react";
import Navbar from "../components/Navbar";

export default function Profile() {
  return (
    <div>
      <Navbar />
      <div className="max-w-3xl mx-auto mt-10">
        <div className="flex gap-10 items-center mb-10">
          <div className="w-32 h-32 rounded-full bg-gray-300"></div>

          <div>
            <h2 className="text-xl font-semibold">alice</h2>
            <div className="flex gap-4 mt-2">
              <span>3 posts</span>
              <span>10 followers</span>
              <span>5 following</span>
            </div>
            <button className="mt-3 border px-4 py-1">
              Follow
            </button>
          </div>
        </div>

        <div className="grid grid-cols-3 gap-2">
          <img src="https://picsum.photos/200" />
          <img src="https://picsum.photos/201" />
          <img src="https://picsum.photos/202" />
        </div>
      </div>
    </div>
  );
}
