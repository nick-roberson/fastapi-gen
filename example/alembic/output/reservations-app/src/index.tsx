import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Import Models

import UserPage from "./components/user_page";

import RestaurantPage from "./components/restaurant_page";

import ReservationPage from "./components/reservation_page";

import ReviewPage from "./components/review_page";

// Layout and other pages
import Home from "./components/Home";
import Layout from "./components/Layout";

export default function HomePage() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          {/* Add other pages here */}
          <Route path="/*" element={<Home />} />
          <Route path="/home" element={<Home />} />

          {/* Add other pages here */}

          <Route path="/user" element={<UserPage />} />

          <Route path="/restaurant" element={<RestaurantPage />} />

          <Route path="/reservation" element={<ReservationPage />} />

          <Route path="/review" element={<ReviewPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement,
);

root.render(<HomePage />);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
