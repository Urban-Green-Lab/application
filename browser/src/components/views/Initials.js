import React, { Component } from 'react';
import {
  Button, Label, Input, Form, FormGroup,
} from 'reactstrap';

class Initials extends Component {
  render() {
    const score = localStorage.getItem('score');
    return (
        <div className="initialsContainer">
          <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit</Button>
          <h1 className="mt-5 score"> {score} pts </h1>
          <p className="mt-2 scoreText"> YOUR SCORE </p>
          <hr />
          <h3 className="mt-2 text-center"> Add your initials to the leaderboard </h3>
          <Form>
            <FormGroup>
              <Label className="m-3" for="initials">Add three letter</Label>
              <Input type="text" name="initials" id="initials" placeholder="initials" maxLength="3" />
              <div className="text-center">
                <Button className="mt-5" size="lg" onClick={this.handleClick} > Add my score </Button>
              </div>
            </FormGroup>
          </Form>
        </div>
    );
  }
}

export default Initials;
