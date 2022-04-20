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
    Button,
    Row,
    Col,
} from "reactstrap";


const Starter = () => {
    return (
        <Row>
            <h3 className="mb-3 mt-3">Lets test it!</h3>
            <Col>
                <CardGroup>
                    <Card>
                        <CardImg alt="Card image cap" src={bg1} top width="100%" />
                        <CardBody>
                            <CardTitle tag="h5">Original Image</CardTitle>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardImg alt="Card image cap" src={bg2} top width="100%" />
                        <CardBody>
                            <CardTitle tag="h5">Grayscale image</CardTitle>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardImg alt="Card image cap" src={bg3} top width="100%" />
                        <CardBody>
                            <CardTitle tag="h5">Colored image</CardTitle>
                        </CardBody>
                    </Card>
                </CardGroup>
                <Row className="mt-3" xs={6}>
                    <Button>Upload</Button>
                    <Button>Convert</Button>
                </Row>
            </Col>
        </Row>
    );
};

export default Starter;
