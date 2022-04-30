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
  export const CustomHandle = ({ style, gt, out }) => {
    const handlePositionChange = useCallback(
      (position) => console.log("[Portrait]", position),
      []
    );
  
    return (
      <ReactCompareSlider
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
            src={out}
            alt="one"
          />
        }
        itemTwo={
          <ReactCompareSliderImage
            src={gt}
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
  
  const Blog = ({gt, out}) => {
    return (
      <Card>
      <CustomHandle position={25} gt={gt} out={out}/>
      </Card>
    );
  };
  
  export default Blog;
  
  