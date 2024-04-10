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
import { getAPIClient, parseField } from "./utils";

// Import Delete Icon
import DeleteIcon from "@mui/icons-material/Delete";

// Import Models
import { {{ model.name }}, {{ model.name }}FromJSON } from "../api";
// Replace with your Host and Port
const basePath = "http://localhost:8000";

function {{ model.name }}Page() {

    // Declare API Client
    const api = getAPIClient();

    // Declare State
    const [{{ model.name.lower() }}, set{{ model.name }}] = useState<{{ model.name }}[]>([]);

    // Fetch Data
    const fetch{{ model.name }}s = async () => {
      const res = await api.get{{ model.name }}s{{ model.name }}sGet();
      set{{ model.name }}(res);
    };

    // Declare Columns for {{ model.name }}
    const {{ model.name.lower() }}_columns = [
        {% for field in model.fields %}
            {% if field.name != "id" %}{ field: "{{ field.camel_case_name }}", headerName: "{{ field.name }}", width: 250 },
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

    // Create {{ model.name }} Models
    const create{{ model.name }} = async () => {
        try {
            let model = {
                id: null,
                {% for field in model.fields %}
                    {% if field.name != "id" %}
                {{ field.camel_case_name }}: parseField(
                    (document.getElementById("{{ field.camel_case_name }}") as HTMLInputElement).value,
                    "{{ field.type }}"
                    ),
                    {% endif %}
                {% endfor %}
            };
            console.log("Creating {{ model.name }}", model)
            let body = {
                {{ model.name.lower() }}: {{ model.name }}FromJSON(model)
            };
            api.create{{ model.name }}{{ model.name }}Post(body).then(() => {
                fetch{{ model.name }}s();
            });
        } catch (e) {
            console.error("Error creating {{ model.name }}", e);
        }
    };


    useEffect(() => {
        fetch{{ model.name }}s();
    }, []);

    return (
        <div>
            <Box m={3}>

                <Box>
                  <Stack direction="row" spacing={2}>
                    <Typography variant="h4">
                      {{ model.name }}s
                    </Typography>
                  </Stack>

                </Box>

                    <Divider> Create {{ model.name }} </Divider>

                    <Grid container spacing={1}>

                        <Grid item xs={12} m={2}>
                            <Stack direction="row" spacing={2}>
                                {% for field in model.fields %}
                                    {% if field.name != "id" %}
                                    <TextField
                                        id="{{ field.camel_case_name }}"
                                        label="{{ field.name }} ({{ field.type }})"
                                        variant="outlined"
                                    />
                                    {% endif %}
                                {% endfor %}
                                <Button
                                    variant="contained"
                                    color="primary"
                                    onClick={ () => { create{{ model.name }}(); } }
                                >
                                    Create {{ model.name }}
                                </Button>
                            </Stack>
                        </Grid>
                    </Grid>

                <Grid container spacing={1}>

                    <Grid item xs={12}>

                        <Divider>
                            <Typography>
                                Loaded { {{ model.name.lower() }}.length } {{ model.name }}s
                            </Typography>
                        </Divider>

                        {
                            {{ model.name.lower() }} && {{ model.name.lower() }}.length > 0 ?
                             <Box m={3}>
                                <DataGrid
                                    rows={ {{ model.name.lower() }} }
                                    columns={ {{ model.name.lower() }}_columns}
                                />
                            </Box>
                            : <p>No {{ model.name }}s found!</p>
                        }

                    </Grid>

                </Grid>
            </Box>
        </div>
    );
}

export default {{ model.name }}Page;
