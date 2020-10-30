import React, { Component } from 'react';
import { Button } from 'reactstrap';
import Celebration from '../images/celebration.png.png';

class Score extends Component {
  render() {
    const score = localStorage.getItem('score');
    return (
        <div className="scoreContainer text-center">
          <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit</Button>
          <img className="centerImg" src={Celebration} alt="Celebration emoji" />
          <h1 className="mt-2 score"> {score} pts </h1>
          <p className="mt-2 scoreText">YOUR SCORE</p>
          <p className="m-3">
            At vero eos et accusamus et iusto odio praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident.
          </p>
          <Button className="mt-5" size="lg" onClick={() => this.props.history.push('/initials')} >View leaderboard</Button>
        </div>
    );
  }
}

export default Score;
