import React, { useEffect, useState } from "react";

// Import MUI Components
import { Box, Typography } from "@mui/material";
import { DataGrid, GridCellParams } from "@mui/x-data-grid";
import { Divider } from "@mui/material";
import { Grid } from "@mui/material";
import { Stack } from "@mui/material";
import { TextField } from "@mui/material";
import { Button } from "@mui/material";

// Import Client
import { DefaultApi } from "../api";
import { Configuration } from "../api";

// Import Delete Icon
import DeleteIcon from "@mui/icons-material/Delete";

// Import Models
import { User, UserFromJSON } from "../api";
// Replace with your Host and Port
const basePath = "http://localhost:8000";

function UserPage() {
  // Declare API Client
  const configuration = new Configuration({
    basePath: basePath,
  });
  const api = new DefaultApi(configuration);

  // Declare State
  const [user, setUser] = useState<User[]>([]);

  // Fetch Data
  const fetchUsers = async () => {
    const res = await api.getUsersUsersGet();
    setUser(res);
  };

  // Declare Columns for User
  const user_columns = [
    { field: "username", headerName: "username", width: 250 },

    { field: "email", headerName: "email", width: 250 },

    { field: "phoneNumber", headerName: "phone_number", width: 250 },

    { field: "preferences", headerName: "preferences", width: 250 },

    { field: "role", headerName: "role", width: 250 },

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

  // Create User Models
  const createUser = async () => {
    try {
      let model = {
        id: null,

        username: (document.getElementById("username") as HTMLInputElement)
          .value,

        email: (document.getElementById("email") as HTMLInputElement).value,

        phoneNumber: (
          document.getElementById("phoneNumber") as HTMLInputElement
        ).value,

        preferences: (
          document.getElementById("preferences") as HTMLInputElement
        ).value,

        role: (document.getElementById("role") as HTMLInputElement).value,
      };
      console.log("Creating User", model);
      let body = {
        user: UserFromJSON(model),
      };
      api.createUserUserPost(body).then(() => {
        fetchUsers();
      });
    } catch (e) {
      console.error("Error creating User", e);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Stack direction="row" spacing={2}>
            <Typography variant="h4">Users</Typography>
          </Stack>
        </Box>

        <Divider> Create User </Divider>

        <Grid container spacing={1}>
          <Grid item xs={12} m={2}>
            <Stack direction="row" spacing={2}>
              <TextField
                id="username"
                label="username (str)"
                variant="outlined"
              />

              <TextField id="email" label="email (str)" variant="outlined" />

              <TextField
                id="phoneNumber"
                label="phone_number (str)"
                variant="outlined"
              />

              <TextField
                id="preferences"
                label="preferences (list)"
                variant="outlined"
              />

              <TextField id="role" label="role (str)" variant="outlined" />

              <Button
                variant="contained"
                color="primary"
                onClick={() => {
                  createUser();
                }}
              >
                Create User
              </Button>
            </Stack>
          </Grid>
        </Grid>

        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Divider>
              <Typography>Loaded {user.length} Users</Typography>
            </Divider>

            {user && user.length > 0 ? (
              <Box m={3}>
                <DataGrid rows={user} columns={user_columns} />
              </Box>
            ) : (
              <p>No Users found!</p>
            )}
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default UserPage;
