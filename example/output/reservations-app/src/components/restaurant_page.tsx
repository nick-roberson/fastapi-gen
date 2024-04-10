import React, { useEffect, useState } from "react";

// Import MUI Components
import { Box, Typography } from "@mui/material";
import { DataGrid, GridCellParams } from "@mui/x-data-grid";
import { Divider } from "@mui/material";
import { Grid } from "@mui/material";
import { Stack } from "@mui/material";

// Import Client
import { DefaultApi } from "../api";
import { Configuration } from "../api";

// Import Delete Icon
import DeleteIcon from "@mui/icons-material/Delete";

// Import Models
import { Restaurant } from "../api";

// Replace with your Host and Port
const basePath = "http://localhost:8000";

function RestaurantPage() {
  // Declare API Client
  const configuration = new Configuration({
    basePath: basePath,
  });
  const api = new DefaultApi(configuration);

  // Declare State
  const [restaurant, setRestaurant] = useState<Restaurant[]>([]);

  // Fetch Data
  const fetchRestaurants = async () => {
    const res = await api.getRestaurantsRestaurantsGet();
    setRestaurant(res);
  };

  // Declare Columns for Restaurant
  const restaurant_columns = [
    { field: "name", headerName: "name", width: 250 },

    { field: "location", headerName: "location", width: 250 },

    { field: "cuisine", headerName: "cuisine", width: 250 },

    { field: "rating", headerName: "rating", width: 250 },

    { field: "priceRange", headerName: "price_range", width: 250 },

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

  useEffect(() => {
    fetchRestaurants();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Stack direction="row" spacing={2}>
            <Typography variant="h4">Restaurants</Typography>
          </Stack>
        </Box>

        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Divider>
              <Typography>Loaded {restaurant.length} Restaurants</Typography>
            </Divider>

            {restaurant && restaurant.length > 0 ? (
              <Box m={3}>
                <DataGrid rows={restaurant} columns={restaurant_columns} />
              </Box>
            ) : (
              <p>No Restaurants found!</p>
            )}

            <Divider> Create Restaurant </Divider>

            <Typography>Coming soon ...</Typography>
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default RestaurantPage;
