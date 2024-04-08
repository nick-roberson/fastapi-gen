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
import { {{ model.name }} } from "../api";

// Replace with your Host and Port
const basePath = "http://localhost:8000";

function {{ model.name }}Page() {

    // Declare API Client
    const configuration = new Configuration({
      basePath: basePath,
    });
    const api = new DefaultApi(configuration);

    // Declare State
    const [{{ model.name.lower() }}, set{{ model.name }}] = useState<{{ model.name }}[]>([]);

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

    // Fetch Data
    const fetch{{ model.name }}s = async () => {
      const res = await api.get{{ model.name }}s{{ model.name }}sGet();
      set{{ model.name }}(res);
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
                      {{ model.name }}s Page
                    </Typography>
                  </Stack>

                </Box>

                <Grid container spacing={1}>

                    <Grid item xs={12}>
                        <Divider> {{ model.name }}s </Divider>
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
