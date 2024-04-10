import React, { useEffect } from "react";
import "./App.css";

// Import MUI Components
import { Container, Box, Typography } from "@mui/material";
import { DataGrid, GridCellParams } from "@mui/x-data-grid";
import { Divider } from "@mui/material";
import { Grid } from "@mui/material";
import { Stack } from "@mui/material";

// Import Client
import { DefaultApi } from "./api";
import { Configuration } from "./api";

// Import Delete Icon
import DeleteIcon from "@mui/icons-material/Delete";

// Import Models

import { User } from "./api";

import { Restaurant } from "./api";

import { Reservation } from "./api";

import { Review } from "./api";

// Replace with your Host and Port
const basePath = "http://localhost:8000";

function App() {
  // Declare API Client
  const configuration = new Configuration({
    basePath: basePath,
  });
  const api = new DefaultApi(configuration);

  // Declare State

  const [user, setUser] = React.useState<User[]>([]);

  const [restaurant, setRestaurant] = React.useState<Restaurant[]>([]);

  const [reservation, setReservation] = React.useState<Reservation[]>([]);

  const [review, setReview] = React.useState<Review[]>([]);

  // Declare Columns for User
  const user_columns = [
    { field: "username", headerName: "username", width: 150 },

    { field: "email", headerName: "email", width: 150 },

    { field: "phoneNumber", headerName: "phone_number", width: 150 },

    { field: "preferences", headerName: "preferences", width: 150 },

    { field: "role", headerName: "role", width: 150 },

    // Delete Button, will call the delete endpoint and reload the data
    {
      field: "delete",
      headerName: "Delete",
      width: 100,
      renderCell: (params: GridCellParams<User>) => {
        return (
          <DeleteIcon
            onClick={() => {
              let model = params.row as User;
              if (!model.id) {
                console.log("Could not find id for deletion", model);
                return;
              }
              api
                .deleteUserUserDelete({ userId: model.id as string })
                .then(() => {
                  fetchUsers();
                });
            }}
          />
        );
      },
    },
  ];

  // Declare Columns for Restaurant
  const restaurant_columns = [
    { field: "name", headerName: "name", width: 150 },

    { field: "location", headerName: "location", width: 150 },

    { field: "cuisine", headerName: "cuisine", width: 150 },

    { field: "rating", headerName: "rating", width: 150 },

    { field: "priceRange", headerName: "price_range", width: 150 },

    // Delete Button, will call the delete endpoint and reload the data
    {
      field: "delete",
      headerName: "Delete",
      width: 100,
      renderCell: (params: GridCellParams<Restaurant>) => {
        return (
          <DeleteIcon
            onClick={() => {
              let model = params.row as Restaurant;
              if (!model.id) {
                console.log("Could not find id for deletion", model);
                return;
              }
              api
                .deleteRestaurantRestaurantDelete({
                  restaurantId: model.id as string,
                })
                .then(() => {
                  fetchRestaurants();
                });
            }}
          />
        );
      },
    },
  ];

  // Declare Columns for Reservation
  const reservation_columns = [
    { field: "restaurantId", headerName: "restaurant_id", width: 150 },

    { field: "userId", headerName: "user_id", width: 150 },

    { field: "reservationTime", headerName: "reservation_time", width: 150 },

    { field: "partySize", headerName: "party_size", width: 150 },

    { field: "specialRequests", headerName: "special_requests", width: 150 },

    // Delete Button, will call the delete endpoint and reload the data
    {
      field: "delete",
      headerName: "Delete",
      width: 100,
      renderCell: (params: GridCellParams<Reservation>) => {
        return (
          <DeleteIcon
            onClick={() => {
              let model = params.row as Reservation;
              if (!model.id) {
                console.log("Could not find id for deletion", model);
                return;
              }
              api
                .deleteReservationReservationDelete({
                  reservationId: model.id as string,
                })
                .then(() => {
                  fetchReservations();
                });
            }}
          />
        );
      },
    },
  ];

  // Declare Columns for Review
  const review_columns = [
    { field: "restaurantId", headerName: "restaurant_id", width: 150 },

    { field: "userId", headerName: "user_id", width: 150 },

    { field: "rating", headerName: "rating", width: 150 },

    { field: "comment", headerName: "comment", width: 150 },

    // Delete Button, will call the delete endpoint and reload the data
    {
      field: "delete",
      headerName: "Delete",
      width: 100,
      renderCell: (params: GridCellParams<Review>) => {
        return (
          <DeleteIcon
            onClick={() => {
              let model = params.row as Review;
              if (!model.id) {
                console.log("Could not find id for deletion", model);
                return;
              }
              api
                .deleteReviewReviewDelete({ reviewId: model.id as string })
                .then(() => {
                  fetchReviews();
                });
            }}
          />
        );
      },
    },
  ];

  // Fetch Data

  const fetchUsers = async () => {
    const res = await api.getUsersUsersGet();
    setUser(res);
  };

  const fetchRestaurants = async () => {
    const res = await api.getRestaurantsRestaurantsGet();
    setRestaurant(res);
  };

  const fetchReservations = async () => {
    const res = await api.getReservationsReservationsGet();
    setReservation(res);
  };

  const fetchReviews = async () => {
    const res = await api.getReviewsReviewsGet();
    setReview(res);
  };

  useEffect(() => {
    fetchUsers();

    fetchRestaurants();

    fetchReservations();

    fetchReviews();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Stack direction="row" spacing={2}>
            <Typography variant="h4">reservations-app</Typography>
            <Typography variant="h6" color="textSecondary">
              1.0.0
            </Typography>
          </Stack>

          <Typography variant="body1">
            A alembic reservations service
          </Typography>
        </Box>

        <Grid container spacing={1}>
          <Grid item xs={6}>
            <Divider> Users </Divider>
            {user && user.length > 0 ? (
              <Box m={3}>
                <DataGrid
                  rows={user}
                  columns={user_columns}
                  density="compact"
                />
              </Box>
            ) : (
              <p>No Users found!</p>
            )}
          </Grid>

          <Grid item xs={6}>
            <Divider> Restaurants </Divider>
            {restaurant && restaurant.length > 0 ? (
              <Box m={3}>
                <DataGrid
                  rows={restaurant}
                  columns={restaurant_columns}
                  density="compact"
                />
              </Box>
            ) : (
              <p>No Restaurants found!</p>
            )}
          </Grid>

          <Grid item xs={6}>
            <Divider> Reservations </Divider>
            {reservation && reservation.length > 0 ? (
              <Box m={3}>
                <DataGrid
                  rows={reservation}
                  columns={reservation_columns}
                  density="compact"
                />
              </Box>
            ) : (
              <p>No Reservations found!</p>
            )}
          </Grid>

          <Grid item xs={6}>
            <Divider> Reviews </Divider>
            {review && review.length > 0 ? (
              <Box m={3}>
                <DataGrid
                  rows={review}
                  columns={review_columns}
                  density="compact"
                />
              </Box>
            ) : (
              <p>No Reviews found!</p>
            )}
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default App;
