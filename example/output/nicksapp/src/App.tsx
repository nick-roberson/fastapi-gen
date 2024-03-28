import React, { useEffect } from "react";
import "./App.css";

// Import MUI Components
import { Container, Box, Typography } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";

// Import Client
import { DefaultApi } from "./api";
import { Configuration } from "./api";

// Import Models

import { User } from "./api";

import { Group } from "./api";

// Declare Columns for DataGrid

const user_columns = [
  { field: "id", headerName: "id", width: 150 },

  { field: "username", headerName: "username", width: 150 },

  { field: "email", headerName: "email", width: 150 },

  { field: "location", headerName: "location", width: 150 },

  { field: "age", headerName: "age", width: 150 },

  { field: "team", headerName: "team", width: 150 },
];

const group_columns = [
  { field: "id", headerName: "id", width: 150 },

  { field: "name", headerName: "name", width: 150 },

  { field: "users", headerName: "users", width: 150 },
];

function App() {
  // Declare API Client
  const configuration = new Configuration({
    basePath: "http://localhost:8000",
  });
  const api = new DefaultApi(configuration);

  // Declare State

  const [user, setUser] = React.useState<User[]>([]);

  const [group, setGroup] = React.useState<Group[]>([]);

  // Fetch Data

  const fetchUser = async () => {
    const res = await api.getUsersUsersGet();
    setUser(res);
  };

  const fetchGroup = async () => {
    const res = await api.getGroupsGroupsGet();
    setGroup(res);
  };

  useEffect(() => {
    fetchUser();

    fetchGroup();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Typography variant="h4">Django React App</Typography>
        </Box>

        <Box>
          <Typography variant="h5">User</Typography>
          <Box m={3}>
            <DataGrid rows={user} columns={user_columns} />
          </Box>
        </Box>

        <Box>
          <Typography variant="h5">Group</Typography>
          <Box m={3}>
            <DataGrid rows={group} columns={group_columns} />
          </Box>
        </Box>
      </Box>
    </div>
  );
}

export default App;
