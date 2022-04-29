import { useState } from "react";
import bg1 from "../../assets/images/bg/bg1.jpg";
import bg2 from "../../assets/images/bg/bg2.jpg";
import bg3 from "../../assets/images/bg/bg3.jpg";
import {Divider, Grid} from '@mui/material';
import {
    Card,
    CardImg,
    CardText,
    CardBody,
    CardTitle,
    CardSubtitle,
    CardGroup,
    CardDeck,
    Button,
    Row,
    Col,
} from "reactstrap";


const Starter = () => {
    const [file, setFile] = useState();
    const [img, setImg] = useState();

    const handleChange = (e) => {
        e.preventDefault();
        console.log(e.target.files[0]);
        setFile(e.target.files[0]);
        setImg(URL.createObjectURL(e.target.files[0]))
    }
    let handleClick = (e) => {
        if(e.target!==e.currentTarget) e.currentTarget.click()
    }


    const Convert = (e) => {
        e.preventDefault()
        const formData = new FormData();
        formData.append('file', file)

        for (var key of formData.entries()) {
            console.log(key[0] + ', ' + key[1]);
        }
        
        const Upload = async() => {
          await fetch('http://localhost:8000/a', {
            method: 'POST',
            body: formData
          }).then(resp => {
            resp.json().then(data => {console.log(data)})
          })
        }
        Upload();
      }

    return (
        <Row>
            <h3 className="mb-3 mt-3">Lets test it!</h3>
            <Col>
                <CardGroup>
                    <Card>
                        <CardImg alt="Card image cap" src={img} top width="256px" height="256px" />
                        <CardBody>
                            <CardTitle tag="h5">Original Image</CardTitle>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardImg alt="Card image cap" src={img} top width="256px" height="256px" />
                        <CardBody>
                            <CardTitle tag="h5">Grayscale image</CardTitle>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardImg alt="Card image cap" src={img} top width="256px" height="256px" />
                        <CardBody>
                            <CardTitle tag="h5">Colored image</CardTitle>
                        </CardBody>
                    </Card>
                </CardGroup>
                {/* <Grid container spacing={0}>

                </Grid> */}
                <Grid container spacing={0} justifyContent="space-evenly" sx={{mt: 3}}>
                    <Grid item alignSelf="center">
                        <input type="file" id="files" onChange={handleChange} style={{display: "none"}}/>
                        <label htmlFor="files" onClick={handleClick}>
                            <Button variant="outline-dark" component="span" style={{width: "100%"}}>
                                Select File
                            </Button>    
                        </label>
                    </Grid>
                    
                    <Divider orientation="vertical" flexItem>
                            OR
                    </Divider>
                    
                    <Grid item xs={6} alignSelf="center" justifySelf="center">
                    {/* <Grid container >
                        <Grid Item
                    </Grid> */}
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus id dignissim justo. etermines a grid item’s location within the grid by referring to specific grid lines. grid-column-start/grid-row-start is the line where the item begins, and grid-column-end/grid-row-end is the line where the item ends.
                        {/* {content} */}
                    </Grid>
                    <Grid item alignSelf="center" justifySelf="center">
                        <Button variant="contained">
                            Convert
                        </Button>
                    </Grid>
                </Grid>
            </Col>
        </Row>
    );
};

export default Starter;
