import React, { useState } from "react";

import "./BackgroundVideo.css";

import Particles from "react-particles-js";

import PhoneInput from "react-phone-number-input";

import { Container, Row, Col } from "reactstrap";
import PlacesAutocomplete from "./PlacesAutocomplete";

import {write} from "../firebase";

const BackgroundVideo = () => {
  const [phoneNumber, setPhoneNumber] = useState();
  const [longitude, setLongitude] = useState();
  const [latitude, setLatitude] = useState();

  function onSubmitInfo()
  {
      if(!longitude || !latitude || !phoneNumber)
      {
          alert("Please fill out all areas.");
      }
      else{
          alert("Thank you for using Twext! You should now receive text notifications about events in your area.");

          let ref = "user/" + phoneNumber;
          let obj = {phoneNumber, longitude, latitude};
          write(ref, obj);
      }
  }

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
          <h1 className="tweet-title">Twext</h1>
          <div className="information-box">
            <h1 className="info-box-words">PERSONAL INFORMATION</h1>
            <Container>
              <Row className="phone-num-row">
                <Col>
                  <h1 className="label-info">Phone Number</h1>
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
              <Row className="phone-num-row">
                <Col>
                  <h1 className="label-info">Location</h1>
                  <button className="submit-button" onClick={onSubmitInfo}>Submit</button>
                </Col>
                <Col>
                  <PlacesAutocomplete
                    setLongitude={setLongitude}
                    setLatitude={setLatitude}
                  ></PlacesAutocomplete>
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
