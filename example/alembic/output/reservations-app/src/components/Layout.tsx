import * as React from "react";
import { Outlet } from "react-router-dom";

// MUI Components
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import Divider from "@mui/material/Divider";
import { ThemeProvider} from '@mui/material';
import { createTheme } from '@mui/material/styles';
import { green, blue } from '@mui/material/colors';


function Layout() {
  // Define the pages and their routes
  const [pages_map] = React.useState<Record<string, string>>({
    Home: "/home",
    User: "/user",
    Restaurant: "/restaurant",
    Reservation: "/reservation",
    Review: "/review",
  });

  // Handle navigation to the page
  const handleNavToPage = (page: string) => {
    console.log("Navigating to page: " + page);
    window.location.href = pages_map[page];
  };

  // Render
  return (
    <>
    <ThemeProvider theme={theme}>
      <nav>
        <AppBar position="static">
          <Box>
            <Toolbar disableGutters>
              <Box m={1}>
                <Typography variant="h5">reservations-app</Typography>
              </Box>

              <Box m={1}>
                {pages_map &&
                  Object.keys(pages_map).map((page) => (
                    <Button
                      color="inherit"
                      onClick={() => handleNavToPage(page)}
                    >
                      {page} Page
                    </Button>
                  ))}
              </Box>
            </Toolbar>
          </Box>
        </AppBar>
      </nav>
      </ThemeProvider>
      <Outlet />
    </>
  );
}
export default Layout;
