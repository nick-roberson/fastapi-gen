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
import { Review, ReviewFromJSON } from "../api";
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

  // Fetch Data
  const fetchReviews = async () => {
    const res = await api.getReviewsReviewsGet();
    setReview(res);
  };

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

  // Create Review Models
  const createReview = async () => {
    try {
      let model = {
        id: null,

        restaurantId: (
          document.getElementById("restaurantId") as HTMLInputElement
        ).value,

        userId: (document.getElementById("userId") as HTMLInputElement).value,

        rating: (document.getElementById("rating") as HTMLInputElement).value,

        comment: (document.getElementById("comment") as HTMLInputElement).value,
      };
      console.log("Creating Review", model);
      let body = {
        review: ReviewFromJSON(model),
      };
      api.createReviewReviewPost(body).then(() => {
        fetchReviews();
      });
    } catch (e) {
      console.error("Error creating Review", e);
    }
  };

  useEffect(() => {
    fetchReviews();
  }, []);

  return (
    <div>
      <Box m={3}>
        <Box>
          <Stack direction="row" spacing={2}>
            <Typography variant="h4">Reviews</Typography>
          </Stack>
        </Box>

        <Divider> Create Review </Divider>

        <Grid container spacing={1}>
          <Grid item xs={12} m={2}>
            <Stack direction="row" spacing={2}>
              <TextField
                id="restaurantId"
                label="restaurant_id (str)"
                variant="outlined"
              />

              <TextField id="userId" label="user_id (str)" variant="outlined" />

              <TextField
                id="rating"
                label="rating (float)"
                variant="outlined"
              />

              <TextField
                id="comment"
                label="comment (str)"
                variant="outlined"
              />

              <Button
                variant="contained"
                color="primary"
                onClick={() => {
                  createReview();
                }}
              >
                Create Review
              </Button>
            </Stack>
          </Grid>
        </Grid>

        <Grid container spacing={1}>
          <Grid item xs={12}>
            <Divider>
              <Typography>Loaded {review.length} Reviews</Typography>
            </Divider>

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
