import { Row, Col, Card, CardBody, CardTitle, Button } from "reactstrap";

const About = () => {
  return (
    <Row>
      <Col>
        {/* --------------------------------------------------------------------------------*/}
        {/* Card-1*/}
        {/* --------------------------------------------------------------------------------*/}
        <Card>
          {/* <CardTitle tag="h6" className="border-bottom p-3 mb-0">
            <i className="bi bi-bell me-2"> </i>
            Colorize Gray images
          </CardTitle> */}
          <CardBody className="p-4">
            <Row justify-content>
              <Col lg="12">
                <h2 className="mt-4">ColorMe</h2>
                <h5 className=" mb-4">
                  This is the frontend for simulating the "Colorful Image Colorization" 2016 paper by Richard Zhang et al.
                  We demontrate colorization of grayscale images as a part of this Computer Vision project.
                </h5>
                <h5 className=" mb-4">
                  Based on DeepLearning. \\ADD STUFF HERE\\
                </h5>
                <h5 className=" mb-4">
                  Credits: <br />
                  1) Pratyush Priyadarshi <br />
                  2) Triansh Sharma <br />
                  3) Raj Maheshwari <br />
                </h5>

                {/* <img
                  src="https://demos.wrappixel.com/free-admin-templates/angular/landingpage-styles/assets/images/screenshots/adminpro-react-pro-lp-img.jpg"
                  alt="my"
                /> */}
                {/* <br /> */}
                {/* <Button
                  className="mt-3"
                  color="primary"
                  href="https://www.wrappixel.com/templates/adminpro-react-redux-admin/?ref=33"
                  target="_blank"
                >
                  Check Pro Version
                </Button> */}
              </Col>
            </Row>
          </CardBody>
        </Card>
      </Col>
    </Row>
  );
};

export default About;
