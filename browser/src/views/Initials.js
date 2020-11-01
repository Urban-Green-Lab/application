import React, { Component } from 'react';
import {
  Button, Input, Form, FormGroup,
} from 'reactstrap';
import postUserInfo from '../data/postUserObject';
import Footer from '../components/Footer';

class Initials extends Component {
  state = {
    initials: '',
  }

  handleClick = (e) => {
    e.preventDefault();
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
      initials: e.target.value.toUpperCase(),
    });
  }

  render() {
    const score = localStorage.getItem('score');
    return (
      <div className="initialsWrapper">
        <div className="initialsContainer">
          <div className="btn-container">
            <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit &nbsp;<i className="fas fa-times"></i></Button>
          </div>
          <h1 className="mt-5 score"> {score}<span className="text-small">pts</span> </h1>
          <p className="mt-2 scoreText"> YOUR SCORE </p>
          <hr />
          <h3 className="mt-2 text-center"> Add your initials to the leaderboard </h3>
          <Form onSubmit={this.handleClick}>
            <div className="text-center">
              <FormGroup>
                <Input className="form-control mt-3 initials-input" type="text" name="initials" id="initials" placeholder="initials" maxLength="3" required onChange={this.handleChange} />
                <Button className="mt-5" size="lg"> Add my score </Button>
              </FormGroup>
            </div>
          </Form>
        </div>
        <Footer />
      </div>
    );
  }
}

export default Initials;
