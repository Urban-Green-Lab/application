import React, { Component } from 'react';
import { Table } from 'reactstrap';
import getLeaderBoardInfo from '../data/getLeaderboardInfo';

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
      <div>
        <div>Exit</div>
        <h1>Leaderboard</h1>
        {this.state.scores && <ScoresTable scores={this.state.scores} />}
      </div>
    );
  }
}

function ScoresTable(props) {
  return (
    <Table borderless>
      <tbody>
        {props.scores.map((s, i) => <tr key={i}>
        <th scope="row">{i + 1}</th>
        <td>{s.intials}</td>
        <td>{s.score}</td>
        </tr>)}
      </tbody>
    </Table>
  );
}
