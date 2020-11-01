import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from '../../views/Home';
import Splash from '../../views/Splash';
import Countdown from '../../views/Countdown';
import Score from '../../views/Score';
import Thanks from '../../views/Thanks';
import Initials from '../../views/Initials';
import Quiz from '../../views/Quiz';
import Leaderboard from '../../views/Leaderboard';

export default class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route
            path='/'
            exact
            component={Splash}
          />
          <Route
            path='/info'
            exact
            component={Home}
          />
           <Route
            path='/countdown'
            exact
            component={Countdown}
          />
          <Route
            path='/score'
            exact
            component={Score}
          />
           <Route
            path='/initials'
            exact
            component={Initials}
          />
          <Route
            path='/thanks'
            exact
            component={Thanks}
            />
            <Route
            exact
            path="/quiz/:id"
            component={(props) => <Quiz {...props} />}
            />
            <Route
            path='/leaderboard'
            exact
            component={Leaderboard}
          />
          <Route path='*' exact={true} component={Splash} />
        </Switch>
      </BrowserRouter>
    );
  }
}
