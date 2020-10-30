import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import UglLogo from '../images/UglLogo.png';

export default class Countdown extends Component {
  state = {
    count: 3,
    running: true,
  };

  componentDidMount() {
    this.handleStart();
  }

  format = (time) => {
    const seconds = time % 60;
    return `${seconds}`;
  };

  handleStart = () => {
    this.timer = setInterval(() => {
      const newCount = this.state.count - 1;
      this.setState({ count: newCount >= 0 ? newCount : 0 });
    }, 1000);
  };

  handleCountdown = (seconds) => {
    this.setState({
      count: seconds,
      running: true,
    });
  };

  renderonDOM = () => {
    const some = this.state.count > 0 ? <><h1 className='crazyTimer count'>{this.format(this.state.count)}</h1><button disabled className='btn btn-blue'>Let's Play</button></> : <><h1 className="count">0</h1><Link to='./quiz/0' className="btn btn-blue">Let's Play</Link></>;
    return some;
  };

  render() {
    return (
      <div className='countdown'>
        <div className="countdown-container">
          <h1>Get ready!</h1>
          {this.renderonDOM()}
        </div>
        <p>brought to you by</p>
        <img src={UglLogo} alt="urban green lab" className="ugl-logo"/>
      </div>
    );
  }
}
