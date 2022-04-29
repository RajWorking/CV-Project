import { useState } from "react";
import bg1 from "../../assets/images/bg/bg1.jpg";
import bg2 from "../../assets/images/bg/bg2.jpg";
import bg3 from "../../assets/images/bg/bg3.jpg";

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

    let handleChange = (e) => {
        e.preventDefault();
        console.log(e.target.files[0]);
        setFile(e.target.files[0]);
        setImg(URL.createObjectURL(e.target.files[0]))
    }

    let Convert = (e) => {
        e.preventDefault();
        console.log(file, typeof(file))
        const data = new FormData();
        data.append('file', file);
        console.log(data)
    
        const submit = async() => {
          await fetch('/api/upload', {
            method: 'POST',
            body: data
          }).then(resp => {
            resp.json().then(data => {console.log(data)})
          })
        }
        submit();
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
                <Row className="mt-3" xs={6}>
                    <Button variant="contained" component="label">
                        <input type="file" onChange={handleChange} />
                    </Button>
                    <Button variant="contained" onClick={Convert}>
                        Convert
                    </Button>
                </Row>
            </Col>
        </Row>
    );
};

export default Starter;
