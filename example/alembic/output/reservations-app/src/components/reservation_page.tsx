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
import { getAPIClient, parseField } from "./utils";

// Import Delete Icon
import DeleteIcon from "@mui/icons-material/Delete";

// Import Models
import { Reservation, ReservationFromJSON } from "../api";
// Replace with your Host and Port
const basePath = "http://localhost:8000";

function ReservationPage() {
  // Declare API Client
  const api = getAPIClient();

  // Declare State
  const [reservation, setReservation] = useState<Reservation[]>([]);

  // Fetch Data
  const fetchReservations = async () => {
    const res = await api.getReservationsReservationsGet();
    setReservation(res);
  };

  // Declare Columns for Reservation
  const reservation_columns = [
    { field: "restaurantId", headerName: "restaurant_id", width: 250 },

    { field: "userId", headerName: "user_id", width: 250 },

    { field: "reservationTime", headerName: "reservation_time", width: 250 },

    { field: "partySize", headerName: "party_size", width: 250 },

    { field: "specialRequests", headerName: "special_requests", width: 250 },

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

  // Create Reservation Models
  const createReservation = async () => {
    try {
      let model = {
        id: null,

        restaurantId: parseField(
          (document.getElementById("restaurantId") as HTMLInputElement).value,
          "int",
        ),

        userId: parseField(
          (document.getElementById("userId") as HTMLInputElement).value,
          "int",
        ),

        reservationTime: parseField(
          (document.getElementById("reservationTime") as HTMLInputElement)
            .value,
          "datetime",
        ),

        partySize: parseField(
          (document.getElementById("partySize") as HTMLInputElement).value,
          "int",
        ),

        specialRequests: parseField(
          (document.getElementById("specialRequests") as HTMLInputElement)
            .value,
          "str",
        ),
      };
      console.log("Creating Reservation", model);
      let body = {
        reservation: ReservationFromJSON(model),
      };
      api.createReservationReservationPost(body).then(() => {
        fetchReservations();
      });
    } catch (e) {
      console.error("Error creating Reservation", e);
    }
  };

  useEffect(() => {
    fetchReservations();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Stack direction="row" spacing={2}>
            <Typography variant="h4">Reservations</Typography>
          </Stack>
        </Box>

        <Divider> Create Reservation </Divider>

        <Grid container spacing={1}>
          <Grid item xs={12} m={2}>
            <Stack direction="row" spacing={2}>
              <TextField
                id="restaurantId"
                label="restaurant_id (int)"
                variant="outlined"
              />

              <TextField id="userId" label="user_id (int)" variant="outlined" />

              <TextField
                id="reservationTime"
                label="reservation_time (datetime)"
                variant="outlined"
              />

              <TextField
                id="partySize"
                label="party_size (int)"
                variant="outlined"
              />

              <TextField
                id="specialRequests"
                label="special_requests (str)"
                variant="outlined"
              />

              <Button
                variant="contained"
                color="primary"
                onClick={() => {
                  createReservation();
                }}
              >
                Create Reservation
              </Button>
            </Stack>
          </Grid>
        </Grid>

        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Divider>
              <Typography>Loaded {reservation.length} Reservations</Typography>
            </Divider>

            {reservation && reservation.length > 0 ? (
              <Box m={3}>
                <DataGrid
                  rows={reservation}
                  columns={reservation_columns}
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
              <p>No Reservations found!</p>
            )}
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default ReservationPage;
