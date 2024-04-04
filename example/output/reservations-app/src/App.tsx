import React, { useEffect } from "react";
import "./App.css";

// Import MUI Components
import { Container, Box, Typography } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { Divider } from "@mui/material";

// Import Client
import { DefaultApi } from "./api";
import { Configuration } from "./api";

// Import Models

import { User } from "./api";

import { Restaurant } from "./api";

import { Reservation } from "./api";

import { Review } from "./api";


// Declare Columns for DataGrid


const user_columns = [




        { field: "username", headerName: "username", width: 150 },



        { field: "email", headerName: "email", width: 150 },



        { field: "phone_number", headerName: "phone_number", width: 150 },



        { field: "preferences", headerName: "preferences", width: 150 },



        { field: "role", headerName: "role", width: 150 },


];



const restaurant_columns = [




        { field: "name", headerName: "name", width: 150 },



        { field: "location", headerName: "location", width: 150 },



        { field: "cuisine", headerName: "cuisine", width: 150 },



        { field: "rating", headerName: "rating", width: 150 },



        { field: "price_range", headerName: "price_range", width: 150 },


];



const reservation_columns = [




        { field: "restaurant_id", headerName: "restaurant_id", width: 150 },



        { field: "user_id", headerName: "user_id", width: 150 },



        { field: "reservation_time", headerName: "reservation_time", width: 150 },



        { field: "party_size", headerName: "party_size", width: 150 },



        { field: "special_requests", headerName: "special_requests", width: 150 },


];



const review_columns = [




        { field: "restaurant_id", headerName: "restaurant_id", width: 150 },



        { field: "user_id", headerName: "user_id", width: 150 },



        { field: "rating", headerName: "rating", width: 150 },



        { field: "comment", headerName: "comment", width: 150 },


];




// Replace with your Host and Port
cost basePath = "http://localhost:8000";

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


    // Fetch Data

    const fetchUser = async () => {
      const res = await api.getUsersUsersGet();
      setUser(res);
    };

    const fetchRestaurant = async () => {
      const res = await api.getRestaurantsRestaurantsGet();
      setRestaurant(res);
    };

    const fetchReservation = async () => {
      const res = await api.getReservationsReservationsGet();
      setReservation(res);
    };

    const fetchReview = async () => {
      const res = await api.getReviewsReviewsGet();
      setReview(res);
    };


    useEffect(() => {

        fetchUser();

        fetchRestaurant();

        fetchReservation();

        fetchReview();

    }, []);

    return (
        <div>
            <Container>
                <Box m={3}>
                    <Box>
                        <Typography variant="h4">My Application</Typography>
                        <p>Generated with FastAPI-React-Generator</p>
                        <p>At the moment the frontend template is very basic, but you can customize it as you wish. Any objects present in the database will be pulled into the tables here and visualized. </p>
                    </Box>

                    <Box m={3}>
                        <Divider> Users </Divider>
                        {
                            user && user.length > 0 ?
                             <Box m={3}>
                                <DataGrid rows={ user } columns={ user_columns}/>
                            </Box>
                            : <p>No Users found!</p>
                        }
                    </Box>

                    <Box m={3}>
                        <Divider> Restaurants </Divider>
                        {
                            restaurant && restaurant.length > 0 ?
                             <Box m={3}>
                                <DataGrid rows={ restaurant } columns={ restaurant_columns}/>
                            </Box>
                            : <p>No Restaurants found!</p>
                        }
                    </Box>

                    <Box m={3}>
                        <Divider> Reservations </Divider>
                        {
                            reservation && reservation.length > 0 ?
                             <Box m={3}>
                                <DataGrid rows={ reservation } columns={ reservation_columns}/>
                            </Box>
                            : <p>No Reservations found!</p>
                        }
                    </Box>

                    <Box m={3}>
                        <Divider> Reviews </Divider>
                        {
                            review && review.length > 0 ?
                             <Box m={3}>
                                <DataGrid rows={ review } columns={ review_columns}/>
                            </Box>
                            : <p>No Reviews found!</p>
                        }
                    </Box>

                </Box>
            </Container>
        </div>
    );
}

export default App;
