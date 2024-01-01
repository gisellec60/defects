import React from 'react'
import "./homestyles.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container'
import Row from  'react-bootstrap/Row'
import Col from  'react-bootstrap/Col'
import { useWindowSize } from "@uidotdev/usehooks";


function Home() {
  const size = useWindowSize
  console.log("this is size", size.width)
  return (
    <div>
      <Container fluid className='noWrap'></Container>
      <Row>
                <Col className="col" >
                    <h1 className='productions-heading'>Defect System </h1> 
                </Col>
         </Row>
    </div>
  )
}

export default Home
