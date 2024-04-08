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
import { Review } from "../api";

// Replace with your Host and Port
const basePath = "http://localhost:8000";

function ReviewPage() {
  // Declare API Client
  const configuration = new Configuration({
    basePath: basePath,
  });
  const api = new DefaultApi(configuration);

  // Declare State
  const [review, setReview] = useState<Review[]>([]);

  // Declare Columns for Review
  const review_columns = [
    { field: "restaurantId", headerName: "restaurant_id", width: 250 },

    { field: "userId", headerName: "user_id", width: 250 },

    { field: "rating", headerName: "rating", width: 250 },

    { field: "comment", headerName: "comment", width: 250 },

    // Delete Button, will call the delete endpoint and reload the data
    {
      field: "delete",
      headerName: "Delete",
      width: 100,
      renderCell: (params: GridCellParams<Review>) => {
        return (
          <DeleteIcon
            onClick={() => {
              let model = params.row as Review;
              if (!model.id) {
                console.log("Could not find id for deletion", model);
                return;
              }
              api
                .deleteReviewReviewDelete({ reviewId: model.id as string })
                .then(() => {
                  fetchReviews();
                });
            }}
          />
        );
      },
    },
  ];

  // Fetch Data
  const fetchReviews = async () => {
    const res = await api.getReviewsReviewsGet();
    setReview(res);
  };

  useEffect(() => {
    fetchReviews();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Stack direction="row" spacing={2}>
            <Typography variant="h4">Reviews Page</Typography>
          </Stack>
        </Box>

        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Divider> Reviews </Divider>
            {review && review.length > 0 ? (
              <Box m={3}>
                <DataGrid rows={review} columns={review_columns} />
              </Box>
            ) : (
              <p>No Reviews found!</p>
            )}
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default ReviewPage;
