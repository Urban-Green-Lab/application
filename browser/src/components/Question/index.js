import React, { Component } from 'react';

export default class Question extends Component {
  render() {
    return (
      <div>
        <h1>{this.props.question.question}</h1>
      </div>
    );
  }
}
