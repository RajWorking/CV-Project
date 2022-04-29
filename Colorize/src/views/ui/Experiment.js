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
    let handleChange = (e) => {
        console.log(e.target.files);
        setFile(URL.createObjectURL(e.target.files[0]));
    }

    return (
        <Row>
            <h3 className="mb-3 mt-3">Lets test it!</h3>
            <Col>
                <CardGroup>
                    <Card>
                        <CardImg alt="Card image cap" src={file} top width="256px" height="256px" />
                        <CardBody>
                            <CardTitle tag="h5">Original Image</CardTitle>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardImg alt="Card image cap" src={file} top width="256px" height="256px" />
                        <CardBody>
                            <CardTitle tag="h5">Grayscale image</CardTitle>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardImg alt="Card image cap" src={file} top width="256px" height="256px" />
                        <CardBody>
                            <CardTitle tag="h5">Colored image</CardTitle>
                        </CardBody>
                    </Card>
                </CardGroup>
                <Row className="mt-3" xs={6}>
                    <Button variant="contained" component="label">
                        <input type="file" onChange={handleChange}/>
                    </Button>
                    <Button variant="contained">
                        Convert
                    </Button>
                </Row>
            </Col>
        </Row>
    );
};

export default Starter;
