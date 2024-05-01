// Simple home page
import React from "react";
import { Link } from "react-router-dom";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";

export function Home() {
  return (
    <Box display="flex" justifyContent="center" height="100vh">
      <div>
        <Typography variant="h3" gutterBottom m={2}>
          Welcome to the restaurant_app!
        </Typography>

        <Typography m={2}>
          To get started, click on one of the links below to view the different
          model pages!
        </Typography>

        <Divider>Models</Divider>

        <Typography variant="h6" gutterBottom m={2}>
          <Link to="/user">Users Page</Link>
        </Typography>

        <Typography variant="h6" gutterBottom m={2}>
          <Link to="/restaurant">Restaurants Page</Link>
        </Typography>

        <Typography variant="h6" gutterBottom m={2}>
          <Link to="/reservation">Reservations Page</Link>
        </Typography>

        <Typography variant="h6" gutterBottom m={2}>
          <Link to="/review">Reviews Page</Link>
        </Typography>
      </div>
    </Box>
  );
}

export default Home;
