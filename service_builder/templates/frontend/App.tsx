import React, { useEffect } from "react";
import "./App.css";

// Import MUI Components
import { Container, Box, Typography } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { Divider } from "@mui/material";

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
                <Box m={3}>
                    <Box>
                        <Typography variant="h4">My Application</Typography>
                        <p>Generated with FastAPI-React-Generator</p>
                        <p>At the moment the frontend template is very basic, but you can customize it as you wish. Any objects present in the database will be pulled into the tables here and visualized. </p>
                    </Box>
                    {% for model in models %}
                    <Box m={3}>
                        <Divider> {{ model.name }}s </Divider>
                        <Box m={3}>
                            <DataGrid rows={ {{ model.name.lower() }} } columns={ {{ model.name.lower() }}_columns}/>
                        </Box>
                    </Box>
                    {% endfor %}
                </Box>
            </Container>
        </div>
    );
}

export default App;
