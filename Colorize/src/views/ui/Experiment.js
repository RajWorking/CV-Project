import { Divider, Grid, Slider, Box } from '@mui/material';
import axios from 'axios';
import { useState , useRef} from 'react';
import { Button, Card, CardBody, CardImg, CardTitle, Col, Row } from 'reactstrap';
import ex1 from '../../assets/images/examples/0_gt.png';
import ex3 from '../../assets/images/examples/1_gt.png';
import ex2 from '../../assets/images/examples/7_gt.png';
import ex1o_n from '../../assets/images/examples/0_out.png';
import ex3o_n from '../../assets/images/examples/1_out.png';
import ex2o_n from '../../assets/images/examples/7_out.png';

const Experiment = ({ label = '', model_type = '', default_outputs }) => {
  const [ex1o, ex2o, ex3o] = default_outputs;

  const hiddenFileInput = useRef(null)

  const [file, setFile] = useState();
  const [img, setImg] = useState();
  const [temp, setTemp] = useState();
  const [outputImage, setOutputImage] = useState();

  const handleChange = (e) => {
    e.preventDefault();
    console.log(e.target.files[0]);
    setFile(e.target.files[0]);
    setImg(URL.createObjectURL(e.target.files[0]));
  };
  // const handleClick = (e) => {
  //   if (e.target !== e.currentTarget) e.currentTarget.click();
  // };

  const handleClick = (e) => {hiddenFileInput.current.click()}

  const Convert = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    formData.append('model_type', model_type);
    formData.append('temp', temp);

    for (var key of formData.entries()) {
      console.log(key[0] + ', ' + key[1]);
    }

    const Upload = async () => {
      const response = await axios.post('http://localhost:8000/a', formData);

      const data = response.data;
      console.log(data);

      console.log(typeof data['input'], data['input']);

      setOutputImage('data:image/jpg;base64,' + data['output']);

      setImg('data:image/jpg;base64,' + data['input']);
    };
    Upload();
  };

  return (
    <Row>
      <h3 className="mb-3 mt-3">{label}</h3>
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
            <label >
            <input type="file" onChange={handleChange} style={{ display: 'none' }} />
              
              <Button variant="outline-dark" component="span" style={{ width: '100%' }} onClick={e => e.target.parentElement.click()}>
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
                    setOutputImage(ex2o);
                  }}
                />
              </Grid>
              <Grid item xs={4} alignSelf="center">
                <CardImg
                  alt="Card image cap"
                  src={ex3}
                  top
                  width="25px"
                  height="100px"
                  onClick={() => {
                    setImg(ex3);
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
      {/* <Box sx={{ backgroundColor: '' }}>
        <Experiment label="Model trained on imagenet" default_outputs={[ex1o_n, ex2o_n, ex3o_n]} />
      </Box> */}
      <Box sx={{ mt: 10, backgroundColor: '' }}>
        <Experiment
          label="Model trained on imagenette"
          model_type="imagenette"
          default_outputs={[ex1o_n, ex2o_n, ex3o_n]}
        />
      </Box>
      <Box sx={{ mt: 10, backgroundColor: '' }}>
        <Experiment
          label="Model trained on landscape dataset"
          model_type="landscape"
          default_outputs={[ex1o_n, ex2o_n, ex3o_n]}
        />
      </Box>
      <Box sx={{ mt: 10, backgroundColor: '' }}>
        <Experiment
          label="Model trained by adding deconv layer"
          model_type="deconv"
          default_outputs={[ex1o_n, ex2o_n, ex3o_n]}
        />
      </Box>
    </Box>
  );
};

export default Starter;
