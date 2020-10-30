import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import Modal from '../components/Modal';
import question from '../images/question.png';
import sustaingame from '../images/sustaingame.png';
import UglLogo from '../images/UglLogo.png';
import floatingBoxes from '../images/floatingBoxes.png';

export default class Splash extends Component {
  render() {
    return (
      <div className="splash">
        <img src={floatingBoxes} alt="" className="bg-img"/>
        <img src={question} alt="question mark" className="question"/>
        <img src={sustaingame} alt="sustain game" className="sustaingame-img"/>
        <p>brought to you by</p>
        <img src={UglLogo} alt="urban green lab" className="ugl-logo"/>
        <Link to='/info' className='btn btn-dark'>Play the Game</Link>
        <Modal buttonLabel={'How to Play'}/>
      </div>
    );
  }
}
