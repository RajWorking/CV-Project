import { Col, Row } from "reactstrap";
import Compare from "../../components/dashboard/Compare";

import gt1 from '../../assets/images/examples/1_gt.png'
import gt2 from '../../assets/images/examples/2_gt.png'
import gt3 from '../../assets/images/examples/3_gt.png'
import gt4 from '../../assets/images/examples/4_gt.png'
import gt5 from '../../assets/images/examples/5_gt.png'
import gt6 from '../../assets/images/examples/6_gt.png'
import gt7 from '../../assets/images/examples/7_gt.png'
import gt8 from '../../assets/images/examples/8_gt.png'
import gt9 from '../../assets/images/examples/9_gt.png'
import gt10 from '../../assets/images/examples/10_gt.png'
import gt11 from '../../assets/images/examples/11_gt.png'
import gt12 from '../../assets/images/examples/12_gt.png'

import out1 from '../../assets/images/examples/1_out.png'
import out2 from '../../assets/images/examples/2_out.png'
import out3 from '../../assets/images/examples/3_out.png'
import out4 from '../../assets/images/examples/4_out.png'
import out5 from '../../assets/images/examples/5_out.png'
import out6 from '../../assets/images/examples/6_out.png'
import out7 from '../../assets/images/examples/7_out.png'
import out8 from '../../assets/images/examples/8_out.png'
import out9 from '../../assets/images/examples/9_out.png'
import out10 from '../../assets/images/examples/10_out.png'
import out11 from '../../assets/images/examples/11_out.png'
import out12 from '../../assets/images/examples/12_out.png'

const Data = [
    {
        gt: gt1,
        out: out1,
    },
    {
        gt: gt2,
        out: out2,
    },
    {
        gt: gt3,
        out: out3,
    },
    {
        gt: gt4,
        out: out4,
    },
    {
        gt: gt5,
        out: out5,
    },
    {
        gt: gt6,
        out: out6,
    },
    {
        gt: gt7,
        out: out7,
    },
    {
        gt: gt8,
        out: out8,
    },{
        gt: gt9,
        out: out9,
    },
    {
        gt: gt10,
        out: out10,
    },
    {
        gt: gt11,
        out: out11,
    },
    {
        gt: gt12,
        out: out12,
    },
];

const Examples = () => {
    return (
        <Row>
            {Data.map(({gt, out}, index) => (
                <Col sm="4" lg="4" xl="4" key={index}>
                    <Compare gt={gt} out={out}/>
                </Col>
            ))}
        </Row>
    );
};

export default Examples;
