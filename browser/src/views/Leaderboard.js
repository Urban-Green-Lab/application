import React, { Component } from 'react';
import { Button, Table } from 'reactstrap';
import getLeaderBoardInfo from '../data/getLeaderboardInfo';
import sustaingame from '../images/sustaingame.png';
import UglLogo from '../images/UglLogo.png';

export default class Leaderboard extends Component {
  state = {
    scores: [],
  }

  componentDidMount() {
    getLeaderBoardInfo().then((resp) => {
      this.setState({
        scores: resp,
      });
    });
  }

  render() {
    return (
      <div className='leaderboard-container'>
        <div className='small-container'>
        <div className="btn-container">
          <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit</Button>
        </div>
          <img src={sustaingame} alt="sustain game" className="sustaingame-img"/>
          <h1>Leaderboard</h1>
    <div className='score-table'>{this.state.scores.length > 0 ? <ScoresTable scores={this.state.scores} /> : <><h4 style={{ textAlign: 'center' }}>Be the first to score!</h4> <Button onClick={() => this.props.history.push('/')}>PLAY NOW</Button></>}</div>
        </div>
        <p>brought to you by</p>
        <img src={UglLogo} alt="urban green lab" className="ugl-logo"/>
      </div>
    );
  }
}

function ScoresTable(props) {
  return (
    <Table borderless>
      <tbody>
        {props.scores.map((s, i) => <tr key={i}>
        <td></td>
        <th scope="row">{i + 1}</th>
        <th scope="row">{s.initials}</th>
        <td className='align-right'>{s.score}pts</td>
        </tr>)}
      </tbody>
    </Table>
  );
}
