import React, { useEffect } from "react";
import "./App.css";

// Import MUI Components
import { Container, Box, Typography } from "@mui/material";
import { DataGrid, GridCellParams } from "@mui/x-data-grid";
import { Divider } from "@mui/material";
import { Grid } from "@mui/material";

// Import Client
import { DefaultApi } from "./api";
import { Configuration } from "./api";

// Import Delete Icon
import DeleteIcon from "@mui/icons-material/Delete";

// Import Models
{% for model in models %}
import { {{ model.name }} } from "./api";
{% endfor %}

// Replace with your Host and Port
const basePath = "http://localhost:8000";

function App() {

    // Declare API Client
    const configuration = new Configuration({
      basePath: basePath,
    });
    const api = new DefaultApi(configuration);

    // Declare State
    {% for model in models %}
    const [{{ model.name.lower() }}, set{{ model.name }}] = React.useState<{{ model.name }}[]>([]);
    {% endfor %}

    {% for model in models %}
    // Declare Columns for {{ model.name }}
    const {{ model.name.lower() }}_columns = [

        {% for field in model.fields %}
            {% if field.name != "id" %}{ field: "{{ field.camel_case_name }}", headerName: "{{ field.name }}", width: 150 },
            {% endif %}
        {% endfor %}

        // Delete Button, will call the delete endpoint and reload the data
        { field: "delete", headerName: "Delete", width: 100, renderCell: (params: GridCellParams<{{model.name}}>) => {
            return (
                <DeleteIcon onClick={() => {
                    let model = params.row as {{model.name}};
                    if (!model.id) {
                        console.log("Could not find id for deletion", model);
                        return;
                    }
                    api.delete{{ model.name }}{{ model.name }}Delete({ {{ model.name.lower() }}Id: model.id as string }).then(() => {
                        fetch{{ model.name }}s();
                    });
                }} />
            );
        }},
    ];
    {% endfor %}


    // Fetch Data
    {% for model in models %}
    const fetch{{ model.name }}s = async () => {
      const res = await api.get{{ model.name }}s{{ model.name }}sGet();
      set{{ model.name }}(res);
    };
    {% endfor %}

    useEffect(() => {
        {% for model in models %}
        fetch{{ model.name }}s();
        {% endfor %}
    }, []);

    return (
        <div>
            <Box m={3}>

                <Box>
                    <Typography variant="h4">My Application</Typography>
                    <p>Generated with FastAPI-React-Generator</p>
                    <p>At the moment the frontend template is very basic, but you can customize it as you wish. Any objects present in the database will be pulled into the tables here and visualized. </p>
                </Box>

                <Grid container spacing={1}>

                    {% for model in models %}
                    <Grid item xs={6}>
                        <Divider> {{ model.name }}s </Divider>
                        {
                            {{ model.name.lower() }} && {{ model.name.lower() }}.length > 0 ?
                             <Box m={3}>
                                <DataGrid
                                    rows={ {{ model.name.lower() }} }
                                    columns={ {{ model.name.lower() }}_columns}
                                    density="compact"
                                />
                            </Box>
                            : <p>No {{ model.name }}s found!</p>
                        }
                    </Grid>
                    {% endfor %}

                </Grid>
            </Box>
        </div>
    );
}

export default App;
