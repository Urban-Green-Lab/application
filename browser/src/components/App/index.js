import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import getActiveEventQuestions from '../../data/getActiveEvent';
import Home from '../../views/Home';

export default class App extends Component {
  state = {
    questions: [],
  };

  componentDidMount() {
    getActiveEventQuestions().then((resp) => {
      this.setState({
        questions: resp,
      });
    });
  }

  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route
            path='/'
            exact
            component={Home}
          />
        </Switch>
      </BrowserRouter>
    );
  }
}
