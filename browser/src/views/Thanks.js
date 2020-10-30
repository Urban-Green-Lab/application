import React, { Component } from 'react';
import { Button } from 'reactstrap';
import UglLogo from '../images/UglLogo.png';

class Thanks extends Component {
  render() {
    return (
      <div className="text-center thanksContainer">
        <div className="wrapper">
          <img src={UglLogo} alt="urban green lab" className="logo"/>
          <h1> Thank you for playing! </h1>
          <p className="m-3">
          To learn more about Urban Green Lab, we encourage you to explore our website. There you'll discover our diverse programs, resources for your home or workplace, and more. </p>
          <p>Be sure to check your email to see your game results and more info!</p>
          <Button className="mt-5">Visit our website</Button>
        </div>
      </div>
    );
  }
}

export default Thanks;
