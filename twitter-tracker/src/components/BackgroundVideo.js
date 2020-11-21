import React, { useState } from "react";

import "./BackgroundVideo.css";

import Particles from "react-particles-js";

import PhoneInput from "react-phone-number-input";

import { Container, Row, Col } from "reactstrap";

import PlacesAutocomplete from "./PlacesAutocomplete";

const BackgroundVideo = () => {
  const [phoneNumber, setPhoneNumber] = useState();
  return (
    <div>
      <Particles
        params={{
          particles: {
            number: {
              value: 1000,
              density: {
                enable: false
              }
            },
            size: {
              value: 3,
              random: true,
              anim: {
                speed: 4,
                size_min: 0.3
              }
            },
            line_linked: {
              enable: false
            },
            move: {
              random: true,
              speed: 1,
              direction: "top",
              out_mode: "out"
            }
          },
          interactivity: {
            events: {
              onhover: {
                enable: true,
                mode: "bubble"
              },
              onclick: {
                enable: true,
                mode: "repulse"
              }
            },
            modes: {
              bubble: {
                distance: 250,
                duration: 2,
                size: 0,
                opacity: 0
              },
              repulse: {
                distance: 400,
                duration: 4
              }
            }
          }
        }}
        style={{
          position: "fixed",
          opacity: "1",
          zIndex: "-3",
          backgroundColor: "black"
        }}
      />
      <div className="Content">
        <div className="SubContent">
          <h1 className="tweet-title">Cool Hackthon Product Name</h1>
          <div className="information-box">
            <h1 className="info-box-words">PERSONAL INFORMATION</h1>
            <Container>
              <Row>
                <Col>
                  <h1>Phone Number</h1>
                </Col>
                <Col>
                  <PhoneInput
                    placeholder="Enter phone number."
                    value={phoneNumber}
                    onChange={setPhoneNumber}
                    defaultCountry="US"
                    className="phone-input"
                  />
                </Col>
              </Row>
              <Row>
                <Col>
                  <h1>Location</h1>
                </Col>
                <Col>
                  <PlacesAutocomplete></PlacesAutocomplete>
                </Col>
              </Row>
            </Container>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BackgroundVideo;
