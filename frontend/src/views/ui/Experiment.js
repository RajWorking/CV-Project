import { Divider, Grid, Slider, Box } from '@mui/material';
import axios from 'axios';
import { useState, useRef } from 'react';
import { Button, Card, CardBody, CardImg, CardTitle, Col, Row } from 'reactstrap';

import empty_img from '../../assets/images/bg/empty.jpg';

import ex1 from '../../assets/images/experiments/1.jpg';
import ex1_net from '../../assets/images/experiments/1_net_out.jpg';
import ex1_nette from '../../assets/images/experiments/1_nette_out.jpg';
import ex1_deconv from '../../assets/images/experiments/1_deconv_out.jpg';
import ex1_land from '../../assets/images/experiments/1_land_out.jpg';

import ex2 from '../../assets/images/experiments/2.png';
import ex2_net from '../../assets/images/experiments/2_net_out.jpeg';
import ex2_nette from '../../assets/images/experiments/2_nette_out.jpeg';
import ex2_deconv from '../../assets/images/experiments/2_deconv_out.jpeg';
import ex2_land from '../../assets/images/experiments/2_land_out.jpeg';

import ex3 from '../../assets/images/experiments/3.png';
import ex3_net from '../../assets/images/experiments/3_net_out.jpeg';
import ex3_nette from '../../assets/images/experiments/3_nette_out.jpeg';
import ex3_deconv from '../../assets/images/experiments/3_deconv_out.jpeg';
import ex3_land from '../../assets/images/experiments/3_land_out.jpeg';

const Experiment = ({ label = '', model_type = '', default_outputs }) => {
  const [ex1o, ex2o, ex3o] = default_outputs;

  const [file, setFile] = useState();
  const [img, setImg] = useState(empty_img);
  const [temp, setTemp] = useState(0.38);
  const [outputImage, setOutputImage] = useState(empty_img);
  const inputEl = useRef(null);

  const handleChange = (e) => {
    e.preventDefault();
    console.log(e.target.files[0]);
    setFile(e.target.files[0]);
    setImg(URL.createObjectURL(e.target.files[0]));
  };

  const Convert = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    formData.append('model_type', model_type);
    formData.append('temp', temp);

    const Upload = async () => {
      const response = await axios.post('http://localhost:8000/a', formData);

      const data = response.data;
      // console.log(data);

      // console.log(typeof data['input'], data['input']);

      setOutputImage('data:image/jpg;base64,' + data['output']);

      setImg('data:image/jpg;base64,' + data['input']);
    };
    Upload();
  };

  return (
    <Row>
      <h3 className="mb-3 mt-3">
        <b>{label}</b>
      </h3>
      <Col>
        <Grid container spacing={3}>
          <Grid item xs={4}>
            <Card>
              <CardImg alt="Card image cap" src={img} top width="256px" height="256px" />
              <CardBody>
                <CardTitle tag="h5">Original Image</CardTitle>
              </CardBody>
            </Card>
          </Grid>
          <Grid item xs={4}>
            <Card>
              <CardImg
                alt="Card image cap"
                src={img}
                style={{ filter: 'grayscale(100%)' }}
                top
                width="256px"
                height="256px"
              />
              <CardBody>
                <CardTitle tag="h5">Grayscale image</CardTitle>
              </CardBody>
            </Card>
          </Grid>
          <Grid item xs={4}>
            <Card>
              <CardImg alt="Card image cap" src={outputImage} top width="256px" height="256px" />
              <CardBody>
                <CardTitle tag="h5">Colored image</CardTitle>
              </CardBody>
            </Card>
          </Grid>
        </Grid>
        <Grid container spacing={0}>
          <Grid item xs={12} sx={{ paddingLeft: 30, paddingRight: 30 }}>
            <Slider
              defaultValue={0.38}
              step={0.01}
              marks
              min={0}
              max={1}
              aria-label="Default"
              valueLabelDisplay="auto"
              onChange={(e, val) => setTemp(val)}
            />
          </Grid>
        </Grid>
        <Grid container spacing={0} justifyContent="space-evenly" sx={{ mt: 3 }}>
          <Grid item alignSelf="center">
            <label>
              <input ref={inputEl} type="file" onChange={handleChange} style={{ display: 'none' }} />

              <Button
                variant="outline-dark"
                component="span"
                style={{ width: '100%' }}
                onClick={(e) => e.target.parentElement.click()}
              >
                Select File
              </Button>
            </label>
          </Grid>

          <Divider orientation="vertical" flexItem>
            OR
          </Divider>

          <Grid item xs={6} alignSelf="center" justifySelf="center">
            <Grid container spacing={1} alignItems="center">
              <Grid item xs={4} alignSelf="center">
                <CardImg
                  alt="Card image cap"
                  src={ex1}
                  top
                  width="25px"
                  height="100px"
                  onClick={() => {
                    if(inputEl.current) {
                      inputEl.current.value = null;
                    }
                    setImg(ex1);
                    setOutputImage(ex1o);
                  }}
                />
              </Grid>
              <Grid item xs={4} alignSelf="center">
                <CardImg
                  alt="Card image cap"
                  src={ex2}
                  top
                  width="25px"
                  height="100px"
                  onClick={() => {
                    setImg(ex2);
                    if(inputEl.current) {
                      inputEl.current.value = null;
                    }
                    setOutputImage(ex2o);
                  }}
                />
              </Grid>
              <Grid item xs={4} alignSelf="center">
                <CardImg
                  alt="Card image cap"center
                  src={ex3}
                  top
                  width="25px"
                  height="100px"
                  onClick={() => {
                    setImg(ex3);
                    if(inputEl.current) {
                      inputEl.current.value = null;
                    }
                    setOutputImage(ex3o);
                  }}
                />
              </Grid>
            </Grid>
            {/* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus id dignissim justo. etermines a grid item’s location within the grid by referring to specific grid lines. grid-column-start/grid-row-start is the line where the item begins, and grid-column-end/grid-row-end is the line where the item ends. */}
            {/* {content} */}
          </Grid>
          <Grid item alignSelf="center" justifySelf="center">
            <Button variant="contained" onClick={(e) => Convert(e)}>
              Convert
            </Button>
          </Grid>
        </Grid>
      </Col>
    </Row>
  );
};

const Starter = () => {
  return (
    <Box>
      <Box sx={{ backgroundColor: '' }}>
        <Experiment
          label="Model trained on Imagenet (10%)"
          default_outputs={[ex1_net, ex2_net, ex3_net]}
        />
      </Box>
      <Divider sx={{ mb: 5, mt: 10 }} />
      <Box>
        <Experiment
          label="Model trained by adding extra Deconvolution layer"
          model_type="deconv"
          default_outputs={[ex1_deconv, ex2_deconv, ex3_deconv]}
        />
      </Box>
      <Divider sx={{ mb: 5, mt: 10 }} />
      <Box>
        <Experiment
          label="Model trained on Imagenette"
          model_type="imagenette"
          default_outputs={[ex1_nette, ex2_nette, ex3_nette]}
        />
      </Box>
      <Divider sx={{ mb: 5, mt: 10 }} />
      <Box>
        <Experiment
          label="Model trained on a Landscape dataset"
          model_type="landscape"
          default_outputs={[ex1_land, ex2_land, ex3_land]}
        />
      </Box>
    </Box>
  );
};

export default Starter;
