import React, { useEffect, useState } from "react";

// Import MUI Components
import { Box, Typography } from "@mui/material";
import { DataGrid, GridCellParams, GridToolbar } from "@mui/x-data-grid";
import { Divider } from "@mui/material";
import { Grid } from "@mui/material";
import { Stack } from "@mui/material";
import { TextField } from "@mui/material";
import { Button } from "@mui/material";

// Import Client
import { getRestaurantAPIClient, parseField } from "./utils";

// Import Delete Icon
import DeleteIcon from "@mui/icons-material/Delete";

// Import Models
import { Restaurant, RestaurantFromJSON } from "../api";
// Replace with your Host and Port
const basePath = "http://localhost:8000";

function RestaurantPage() {
  // Declare API Client
  const api = getRestaurantAPIClient();

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

  // Create Restaurant Models
  const createRestaurant = async () => {
    try {
      let model = {
        id: null,

        name: parseField(
          (document.getElementById("name") as HTMLInputElement).value,
          "str",
        ),

        location: parseField(
          (document.getElementById("location") as HTMLInputElement).value,
          "str",
        ),

        cuisine: parseField(
          (document.getElementById("cuisine") as HTMLInputElement).value,
          "str",
        ),

        rating: parseField(
          (document.getElementById("rating") as HTMLInputElement).value,
          "float",
        ),

        priceRange: parseField(
          (document.getElementById("priceRange") as HTMLInputElement).value,
          "str",
        ),
      };
      console.log("Creating Restaurant", model);
      let body = {
        restaurant: RestaurantFromJSON(model),
      };
      api.createRestaurantRestaurantPost(body).then(() => {
        fetchRestaurants();
      });
    } catch (e) {
      console.error("Error creating Restaurant", e);
    }
  };

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

        <Divider> Create Restaurant </Divider>

        <Grid container spacing={1}>
          <Grid item xs={12} m={2}>
            <Stack direction="row" spacing={2}>
              <TextField id="name" label="name (str)" variant="outlined" />

              <TextField
                id="location"
                label="location (str)"
                variant="outlined"
              />

              <TextField
                id="cuisine"
                label="cuisine (str)"
                variant="outlined"
              />

              <TextField
                id="rating"
                label="rating (float)"
                variant="outlined"
              />

              <TextField
                id="priceRange"
                label="price_range (str)"
                variant="outlined"
              />

              <Button
                variant="contained"
                color="primary"
                onClick={() => {
                  createRestaurant();
                }}
              >
                Create Restaurant
              </Button>
            </Stack>
          </Grid>
        </Grid>

        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Divider>
              <Typography>Loaded {restaurant.length} Restaurants</Typography>
            </Divider>

            {restaurant && restaurant.length > 0 ? (
              <Box m={3}>
                <DataGrid
                  rows={restaurant}
                  columns={restaurant_columns}
                  density="compact"
                  initialState={{
                    pagination: {
                      paginationModel: { page: 0, pageSize: 10 },
                    },
                  }}
                  pageSizeOptions={[10, 20, 50]}
                  slots={{ toolbar: GridToolbar }}
                />
              </Box>
            ) : (
              <p>No Restaurants found!</p>
            )}
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default RestaurantPage;
