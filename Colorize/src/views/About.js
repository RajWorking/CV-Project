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
                  This is the website for simulating the "Colorful Image Colorization" 2016 paper by Richard Zhang et al.
                  We demontrate colorization of grayscale images. This project is part of a course offering (Computer Vision at IIIT-H).
                </h5>
                <h5 className=" mb-4">
                The Examples tab show good and bad results of the Imagenet trained original architecture model for a quick glance.<br/><br/>
                  Experiments Tab shows all the various models' results and on which datasets it has been trained on. The vairious models are:<br/>
                  <ol>
                    <li>10% Imagenet on the original paper architecture.</li>
                    <li>10% Imagenet with an added Deconvolution layer in the original architecture.</li>
                    <li>100% Imagenette on the original paper architecture</li>
                    <li>100% Landscape dataset relearned on the pretrained first model weights with same architecture</li>
                  </ol>
                  You can also upload you <b>own images</b> in the experiments tab to check the models results. Have fun exploring the reuslts. 😄<br/><br/>
                  

                  <b>Based on DeepLearning. Made with Love ❤️ </b>
                </h5>
                <h5 className=" mb-4">
                  Credits: <br />
                  <ol>
                    <li>Pratyush Priyadarshi (2019101118)</li>
                    <li>Triansh Sharma (2019101006)</li> 
                    <li>Raj Maheshwari (2019101039)</li>
                  </ol>
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
