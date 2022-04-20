import {
    Card,
    CardBody,
    CardImg,
    CardSubtitle,
    CardText,
    CardTitle,
    Button,
  } from "reactstrap";
  
  import { useCallback } from "react";
  
  import {
    ReactCompareSlider,
    ReactCompareSliderHandle,
    ReactCompareSliderImage
  } from "react-compare-slider";
  
  /** With Customised `handle`. */
  export const CustomHandle = ({ style, ...props }) => {
    const handlePositionChange = useCallback(
      (position) => console.log("[Portrait]", position),
      []
    );
  
    return (
      <ReactCompareSlider
        {...props}
        handle={
          <ReactCompareSliderHandle
            buttonStyle={{
              backdropFilter: undefined,
              background: "white",
              border: 0,
              color: "#333"
            }}
          />
        }
        itemOne={
          <ReactCompareSliderImage
            src="https://images.unsplash.com/photo-1580458148391-8c4951dc1465?auto=format&fit=crop&w=1280&q=80"
            style={{ filter: "grayscale(1)" }}
            alt="one"
          />
        }
        itemTwo={
          <ReactCompareSliderImage
            src="https://images.unsplash.com/photo-1580458148391-8c4951dc1465?auto=format&fit=crop&w=1280&q=80"
            alt="two"
          />
        }
        onPositionChange={handlePositionChange}
        style={{
          display: "flex",
          width: "100%",
          height: "50vh",
          ...style
        }}
      />
    );
  };
  
  const Blog = (props) => {
    return (
      <Card>
      <CustomHandle position={25} />
      </Card>
    );
  };
  
  export default Blog;
  
  