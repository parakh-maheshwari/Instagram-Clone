Instagram Clone

This is a full-stack Instagram Clone built using FastAPI, MongoDB, React (Vite), and Tailwind CSS.

The project includes user authentication, posts, likes, comments, follow system, and a personalized feed.

Tech Stack
Backend

FastAPI

MongoDB Atlas

JWT Authentication

Python

Frontend

React (Vite)

Tailwind CSS

Axios

React Router DOM

Features
Authentication

User signup

User login

JWT-based authentication

Protected routes

Users

View profile

Follow / unfollow users

View follower and following count

Posts

Create post (image URL + caption)

View posts

Like and unlike posts

Comment on posts

Feed

Personalized feed

Shows posts from followed users only

Project Structure
Instagram Clone/
├── instagram_clone_backend/
│   ├── app/
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── main.py
│
├── instagram_clone_frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── api/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json

How to Run Backend
cd instagram_clone_backend
uvicorn app.main:app --reload


Backend runs on:

http://127.0.0.1:8000

How to Run Frontend
cd instagram_clone_frontend
npm install
npm run dev


Frontend runs on:

http://localhost:5173
