import React, { Component } from 'react';
import { Button } from 'reactstrap';
import partypopper from '../images/partypopper.png';
import floatingBoxes from '../images/floatingBoxes.png';
import UglLogo from '../images/UglLogo.png';

class Score extends Component {
  getMessage() {
    const numScore = Number(localStorage.getItem('score'));
    let message = '';
    if (numScore <= 250) {
      message = 'Beginner: We\'re all at different points in our sustainability journey. Head over to Urban Green Lab\'s website to learn more and boost that score up!';
    } else if (numScore <= 600) {
      message = 'Novice: Not bad but there is some room for improvement. Hang in there and keep learning!';
    } else if (numScore <= 850) {
      message = 'Skilled: Seems like you\'re well on your wat to becoming an expert, keep it';
    } else {
      message = 'Expert: Wow! Check you out, we\'ve got a sustainability expert over here!';
    }
    return message;
  }

  render() {
    const score = localStorage.getItem('score');
    return (
        <div className="scoreContainer text-center">
          <img src={floatingBoxes} alt="" className="bg-img"/>

          <div className="score-body">
            <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit</Button>
            <img className="centerImg" src={partypopper} alt="party popper emoji" />
            <h1 className="mt-2 score">{score}<span>pts</span> </h1>
            <p className="mt-2 scoreText">YOUR SCORE</p>
            <p className="m-3">
              {this.getMessage()}
            </p>
            <Button className="btn-dark btn" onClick={() => this.props.history.push('/initials')} >View leaderboard</Button>
          </div>

          <p>brought to you by</p>
          <img src={UglLogo} alt="urban green lab" className="ugl-logo"/>
        </div>
    );
  }
}

export default Score;
