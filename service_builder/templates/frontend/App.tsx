import React, { useEffect } from "react";
import "./App.css";

// Import MUI Components 
import { Container, Box, Typography } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";

// Import Client 
import { DefaultApi } from "./api";
import { Configuration } from "./api";

// Import Models
{% for model in models %}
import { {{ model.name }} } from "./api";
{% endfor %}

// Declare Columns for DataGrid
{% for model in models %}
const {{ model.name.lower() }}_columns = [
  {% for field in model.fields %}
  { field: "{{ field.name }}", headerName: "{{ field.name }}", width: 150 },
  {% endfor %}
];
{% endfor %}

function App() {

    // Declare API Client
    const configuration = new Configuration({
      basePath: "http://localhost:8000",
    });
    const api = new DefaultApi(configuration);

    // Declare State
    {% for model in models %}
    const [{{ model.name.lower() }}, set{{ model.name }}] = React.useState<{{ model.name }}[]>([]);
    {% endfor %}

    // Fetch Data
    {% for model in models %}
    const fetch{{ model.name }} = async () => {
      const res = await api.get{{ model.name }}s{{ model.name }}sGet();
      set{{ model.name }}(res);
    };
    {% endfor %}

    useEffect(() => {
        {% for model in models %}
        fetch{{ model.name }}();
        {% endfor %}
    }, []);
  
    return (
        <div>
            <Container>
                <Box>
                    <Typography variant="h4">Django React App</Typography>
                </Box>
                {% for model in models %}
                <Box>
                    <Typography variant="h5">{{ model.name }}</Typography>
                    <Box m={3}>
                        <DataGrid rows={ {{ model.name.lower() }} } columns={ {{ model.name.lower() }}_columns}/>
                    </Box>
                </Box>
                {% endfor %}
            </Container>
        </div>
    );
}

export default App;
