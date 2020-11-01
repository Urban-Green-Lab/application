import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import Modal from '../components/Modal';
import NoActiveEvents from '../components/Modal/NoActiveEvents';
import question from '../images/question.png';
import sustaingame from '../images/sustaingame.png';
import getActiveEvent from '../data/getActiveEvent';
import Footer from '../components/Footer';

export default class Splash extends Component {
  state = {
    activeEvent: true,
    childMode: false,
    loading: true,
  }

  componentDidMount() {
    localStorage.setItem('user', JSON.stringify({}));
    getActiveEvent().then((resp) => {
      if (resp === 'NOPE') {
        this.setState({
          activeEvent: false,
        });
      } else {
        this.setState({
          childMode: resp.child_mode,
          loading: false,
        });
      }
    });
  }

  render() {
    return (
      <div className="splash">
        <img src={question} alt="question mark" className="question"/>
        <img src={sustaingame} alt="sustain game" className="sustaingame-img"/>
        <Footer />
        { this.state.loading ? '' : <Link to={this.state.childMode ? '/countdown' : '/info'} className='btn btn-dark mb-4'>Play the Game</Link>}
        { !this.state.activeEvent && <NoActiveEvents buttonLabel={'Game Coming Soon!'}/>}
        <Modal buttonLabel={'How to Play'}/>
      </div>
    );
  }
}
