import React, { useEffect, useState } from "react";

// Import MUI Components
import { Container, Box, Typography } from "@mui/material";
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
import { Reservation } from "../api";

// Replace with your Host and Port
const basePath = "http://localhost:8000";

function ReservationPage() {
  // Declare API Client
  const configuration = new Configuration({
    basePath: basePath,
  });
  const api = new DefaultApi(configuration);

  // Declare State
  const [reservation, setReservation] = useState<Reservation[]>([]);

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

  // Fetch Data
  const fetchReservations = async () => {
    const res = await api.getReservationsReservationsGet();
    setReservation(res);
  };

  useEffect(() => {
    fetchReservations();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Stack direction="row" spacing={2}>
            <Typography variant="h4">Reservations Page</Typography>
          </Stack>
        </Box>

        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Divider> Reservations </Divider>
            {reservation && reservation.length > 0 ? (
              <Box m={3}>
                <DataGrid rows={reservation} columns={reservation_columns} />
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
