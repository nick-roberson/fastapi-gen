// Simple home page
import React from 'react';
import { Link } from 'react-router-dom';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';

export function Home() {
  return (
    <Box display="flex" justifyContent="center" height="100vh">
        <div>
            <Typography variant="h3" gutterBottom m={2}>
                Welcome to the {{ config.service_info.name }}!
            </Typography>

            <Typography m={2}>
                To get started, click on one of the links below to view the different model pages!
            </Typography>

            <Divider>
                Models
            </Divider>

            {% for model in config.models %}
                <Typography variant="h6" gutterBottom m={2}>
                    <Link to="/{{ model.name|lower }}">{{ model.name }}s Page</Link>
                </Typography>
            {% endfor %}
        </div>
    </Box>
  );
}

export default Home;
