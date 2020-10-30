import React, { Component } from 'react';
import {
  Button, Label, Input, Form, FormGroup,
} from 'reactstrap';
import postUserInfo from '../data/postUserObject';
import UglLogo from '../images/UglLogo.png';

class Initials extends Component {
  state = {
    initials: '',
  }

  handleClick = () => {
    const eventId = JSON.parse(localStorage.getItem('event_id'));
    const quizBank = JSON.parse(localStorage.getItem('quiz_bank'));
    const score = JSON.parse(localStorage.getItem('score'));
    const userObj = JSON.parse(localStorage.getItem('user'));
    userObj.initials = this.state.initials;
    userObj.event = eventId;
    userObj.quiz_bank = quizBank;
    userObj.score = score;
    localStorage.setItem('user', JSON.stringify(userObj));

    const newUserObj = JSON.parse(localStorage.getItem('user'));
    postUserInfo(newUserObj).then(() => {
      this.props.history.push('/leaderboard');
    });
  }

  handleChange = (e) => {
    this.setState({
      initials: e.target.value,
    });
  }

  render() {
    const score = localStorage.getItem('score');
    return (
      <div className="initialsWrapper">
        <div className="initialsContainer">
          <div className="btn-container">
            <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit</Button>
          </div>
          <h1 className="mt-5 score"> {score} <span className="text-small">pts</span> </h1>
          <p className="mt-2 scoreText"> YOUR SCORE </p>
          <hr />
          <h3 className="mt-2 text-center"> Add your initials to the leaderboard </h3>
          <Form>
            <FormGroup>
              <Label className="input-label" for="initials">Add three letters</Label>
              <Input className="form-control" type="text" name="initials" id="initials" placeholder="initials" maxLength="3" onChange={this.handleChange} />
              <div className="text-center">
                <Button className="mt-5" size="lg" onClick={this.handleClick} > Add my score </Button>
              </div>
            </FormGroup>
          </Form>
        </div>
        <p>brought to you by</p>
        <img src={UglLogo} alt="urban green lab" className="ugl-logo"/>
      </div>
    );
  }
}

export default Initials;
