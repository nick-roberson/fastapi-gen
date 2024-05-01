import { Configuration } from "../api";

import { UserApi } from "../api";

import { RestaurantApi } from "../api";

import { ReservationApi } from "../api";

import { ReviewApi } from "../api";

const basePath = "http://localhost:8000";

// Helper function to parse fields based on their type prior to sending to the API
const parseField = (field: string, type: string) => {
  switch (type) {
    case "string":
      return field;
    case "number":
      return Number(field);
    case "boolean":
      return field === "true";
    case "date":
      return new Date(field);
    case "datetime":
      return new Date(field);
    case "array":
      return field.split(",").map((item) => (item as string).trim());
    case "list":
      return field.split(",").map((item) => (item as string).trim());
    case "object":
      return JSON.parse(field);
    default:
      return field;
  }
};

// Fetch API client for User
const getUserAPIClient = () => {
  const apiConfig = new Configuration({
    basePath: basePath,
  });
  return new UserApi(apiConfig);
};

// Fetch API client for Restaurant
const getRestaurantAPIClient = () => {
  const apiConfig = new Configuration({
    basePath: basePath,
  });
  return new RestaurantApi(apiConfig);
};

// Fetch API client for Reservation
const getReservationAPIClient = () => {
  const apiConfig = new Configuration({
    basePath: basePath,
  });
  return new ReservationApi(apiConfig);
};

// Fetch API client for Review
const getReviewAPIClient = () => {
  const apiConfig = new Configuration({
    basePath: basePath,
  });
  return new ReviewApi(apiConfig);
};

// Export all API clients and utility functions
export {
  getUserAPIClient,
  getRestaurantAPIClient,
  getReservationAPIClient,
  getReviewAPIClient,
  parseField,
};
