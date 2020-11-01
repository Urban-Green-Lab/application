import React, { Component } from 'react';
import { Button, Table } from 'reactstrap';
import getLeaderBoardInfo from '../data/getLeaderboardInfo';
import sustaingame from '../images/sustaingame.png';
import Footer from '../components/Footer';

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
          <Button className="closeBtn" onClick={() => this.props.history.push('/thanks')}>Exit &nbsp;<i className="fas fa-times"></i></Button>
        </div>
          <img src={sustaingame} alt="sustain game" className="sustaingame-img"/>
          <h1>Leaderboard</h1>
    <div className='score-table'>{this.state.scores.length > 0 ? <ScoresTable scores={this.state.scores} /> : <><h4 style={{ textAlign: 'center' }}>Be the first to score!</h4> <Button onClick={() => this.props.history.push('/')}>PLAY NOW</Button></>}</div>
        </div>
        <Footer />
      </div>
    );
  }
}

function ScoresTable(props) {
  return (
    <Table borderless>
      <tbody>
        {props.scores.map((s, i) => <tr key={i}>
        <td>{i === 0 ? <>&#129351;</> : '' } { i === 1 ? <>&#129352;</> : '' } {i === 2 ? <>&#129353;</> : ''}</td>
        <th scope="row">{i + 1}</th>
        <th scope="row">{s.initials}</th>
        <td className='align-right'>{s.score}pts</td>
        </tr>)}
      </tbody>
    </Table>
  );
}
