import { Col, Row } from "reactstrap";
import Compare from "../../components/dashboard/Compare";

import bg1 from "../../assets/images/bg/bg1.jpg";
import bg2 from "../../assets/images/bg/bg2.jpg";
import bg3 from "../../assets/images/bg/bg3.jpg";
import bg4 from "../../assets/images/bg/bg4.jpg";

const Data = [
    {
        image: bg1,
        title: "Simple is beautiful",
    },
    {
        image: bg2,
        title: "Simple is beautiful",
    },
    {
        image: bg3,
        title: "Simple is beautiful",
    },
    {
        image: bg4,
        title: "Simple is beautiful",
    },
];

const Examples = () => {
    return (
        <Row>
            {Data.map((blg, index) => (
                <Col sm="6" lg="6" xl="6" key={index}>
                    <Compare />
                </Col>
            ))}
        </Row>
    );
};

export default Examples;
