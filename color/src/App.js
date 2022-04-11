import React, { useState } from "react";
import { Grid, Button, Box } from '@mui/material';

function App() {
  const [file, setFile] = useState();
  let handleChange = (e) => {
    console.log(e.target.files);
    setFile(URL.createObjectURL(e.target.files[0]));
  }

  return (
    <div>
      <Grid container justifyContent="center" padding={2}>
        <Grid container spacing={1} padding={2} item xs={4} align="center">
          <Grid item xs={12}>
            <h2>Gray Image</h2>
          </Grid>
          <Grid item xs={12}>
            <Box
              component="img"
              sx={{
                minHeight: { xs: 350 },
                minWidth: { xs: 400 },
                maxHeight: { xs: 400 },
                maxWidth: { xs: 500 }
              }}
              // alt="original image"
              style={{ border: "1px solid grey" }}
              src={file}
            />
          </Grid>
        </Grid>

        <Grid item xs={1} alignItems="center" display="flex">
          <Button variant="contained" component="label">
            <input type="file" onChange={handleChange} hidden />
            Choose file
          </Button>
        </Grid>

        <Grid container spacing={1} padding={2} item xs={4} align="center">
          <Grid item xs={12}>
            <h2>Colored Image</h2>
          </Grid>
          <Grid item xs={12}>
            <Box
              component="img"
              sx={{
                minHeight: { xs: 350 },
                minWidth: { xs: 400 },
                maxHeight: { xs: 400 },
                maxWidth: { xs: 500 }
              }}
              // alt="original image"
              style={{ border: "1px solid grey" }}
              src={file}
            />
          </Grid>
        </Grid>
      </Grid>

    </div>

  );
}

export default App;