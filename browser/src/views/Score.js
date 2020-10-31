import React, { Component } from 'react';
import { Button } from 'reactstrap';
import partypopper from '../images/partypopper.png';
import floatingBoxes from '../images/floatingBoxes.png';
import Footer from '../components/Footer';

class Score extends Component {
  getMessage() {
    const numScore = Number(localStorage.getItem('score'));
    let message = '';
    if (numScore <= 250) {
      message = <><h1>Beginner</h1> <p>We're all at different points in our sustainability journey. Head over to Urban Green Lab's website to learn more and boost that score up!</p></>;
    } else if (numScore <= 600) {
      message = <><h1>Novice</h1><p>Not bad but there is some room for improvement. Hang in there and keep learning!</p></>;
    } else if (numScore <= 850) {
      message = <><h1>Skilled</h1> <p>Seems like you're well on your wat to becoming an expert, keep it</p></>;
    } else {
      message = <><h1>Expert</h1> <p>Wow! Check you out, we've got a sustainability expert over here!</p></>;
    }
    return message;
  }

  render() {
    const score = localStorage.getItem('score');
    return (
        <div className="scoreContainer text-center">
          <img src={floatingBoxes} alt="" className="bg-img"/>

          <div className="score-body">
            <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit &nbsp;<i className="fas fa-times"></i></Button>
            <img className="centerImg" src={partypopper} alt="party popper emoji" />
            <h1 className="mt-2 score">{score}<span>pts</span> </h1>
            <p className="mt-2 scoreText">YOUR SCORE</p>
            <div className="m-3 score-level-text">
              {this.getMessage()}
            </div>
            <Button className="btn-dark btn" onClick={() => this.props.history.push('/initials')} >View leaderboard</Button>
          </div>

          <Footer />
        </div>
    );
  }
}

export default Score;
