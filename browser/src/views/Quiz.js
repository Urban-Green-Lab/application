import React, { Component } from 'react';
import { Alert } from 'reactstrap';
import getActiveEvent from '../data/getActiveEvent';
import Question from '../components/Question';
import Answers from '../components/Answers';
import Footer from '../components/Footer';
import sadface from '../images/sadface.png';
import happyface from '../images/happyface.png';

export default class Quiz extends Component {
  state = {
    questions: [],
    timer: 10,
    score: 0,
    count: 10,
    is_correct: '',
  };

  componentDidMount() {
    getActiveEvent().then((resp) => {
      console.warn(resp);
      localStorage.setItem('event_id', resp.event_id);
      localStorage.setItem('quiz_bank', resp.quiz_id);
      localStorage.setItem('questions', resp.questions.length);
      this.setState({
        questions: resp.questions,
        quiz_bank: resp.quiz_id,
        event_id: resp.event_id,
      }, this.handleStart);
    });
  }

  componentWillUnmount() {
    clearInterval(this.timer);
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
    });
  };

  runIt = (id, qpoints, i) => {
    if (i === 'time') {
      document.querySelector('.c').classList.add('correct');

      this.setState({
        is_correct: '',
        current_value: '',
        current_bp: '',
        count: this.state.timer,
      });

      if (this.state.questions.length > Number(id) + 1) {
        document.querySelector('.c').classList.remove('correct');
        this.props.history.push(`./${Number(id) + 1}`);
      } else {
        localStorage.setItem('score', JSON.stringify(this.state.score));
        this.props.history.push('/score');
      }
    } else {
      console.warn('Time NOT Up!');
      if (this.state.questions.length >= Number(id) + 1) {
        document.querySelector('.c').classList.remove('correct');
        document.querySelector(`#button-${i}`).classList.remove('wrong');
        const bonusPoints = this.state.count * 10;
        const score = qpoints ? bonusPoints + 0 : 0;
        this.setState({
          score: this.state.score + score,
          is_correct: qpoints,
          current_value: 0,
          current_bp: bonusPoints,
          count: this.state.timer,
        });

        if (qpoints) {
          document.querySelector('.c').classList.add('correct');
          setTimeout(() => {
            this.setState({
              is_correct: '',
              current_value: '',
              current_bp: '',
              count: this.state.timer,
            });

            if (this.state.questions.length > Number(id) + 1) {
              document.querySelector('.c').classList.remove('correct');
              document.querySelector(`#button-${i}`).classList.remove('wrong');
              document.querySelector(`#button-${i}`).blur();
              this.props.history.push(`./${Number(id) + 1}`);
            } else {
              localStorage.setItem('score', JSON.stringify(this.state.score));
              this.props.history.push('/score');
            }
          }, 5000);
        } else {
          document.querySelector(`#button-${i}`).classList.remove('wrong');
          document.querySelector('.c').classList.remove('correct');
          document.querySelector('.c').classList.add('correct');
          document.querySelector(`#button-${i}`).classList.add('wrong');
          setTimeout(() => {
            this.setState({
              is_correct: '',
              current_value: '',
              current_bp: '',
              count: this.state.timer,
            });
            if (this.state.questions.length > Number(id) + 1) {
              document.querySelector('.c').classList.remove('correct');
              document.querySelector(`#button-${i}`).classList.remove('wrong');
              document.querySelector(`#button-${i}`).blur();
              this.props.history.push(`./${Number(id) + 1}`);
            } else {
              localStorage.setItem('score', JSON.stringify(this.state.score));
              this.props.history.push('/score');
            }
          }, 5000);
        }
      } else {
        localStorage.setItem('score', JSON.stringify(this.state.score));
        this.props.history.push('/score');
      }
    }
  };

  renderMiddleSection = () => {
    let view;
    if (this.state.is_correct === '') {
      view = <h1 className='crazyTimer'>{this.format(this.state.count)}</h1>;
    } else if (this.state.is_correct) {
      view = <Alert className='score-info'>
      <div className='correct-emoji'>
        <img src={happyface} alt="happy face emoji"/>
      </div>
      <div className="result">
        <p className="correct-result">CORRECT</p>
        <p className="correct-bonus">BONUS +{this.state.current_bp} for fast answer</p>
      </div>
    </Alert>;
    } else {
      view = <Alert className='score-info'>
      <div className='correct-emoji'>
        <img src={sadface} alt="sad face emoji"/>
      </div>
      <div className="result">
        <p className="wrong-result">Wrong Answer</p>
        <p className="wrong-points">0pts</p>
      </div>
    </Alert>;
    }
    return view;
  }

  renderAnswerButtons = () => {
    let view;
    if (this.state.is_correct === '') {
      view = <Answers disabled={false} a={this.state.questions[this.props.match.params.id].answers} click={this.runIt} id={this.props.match.params.id} />;
    } else if (this.state.is_correct) {
      view = <Answers disabled={true} a={this.state.questions[this.props.match.params.id].answers} click={this.runIt} id={this.props.match.params.id} />;
    } else {
      view = <Answers disabled={true} a={this.state.questions[this.props.match.params.id].answers} click={this.runIt} id={this.props.match.params.id} />;
    }
    return view;
  }

  renderonDOM = () => {
    const some = <>
          {this.state.questions.length > 0 ? this.renderQuestion() : 'Question Loading...'}
          {this.state.questions.length > 0 ? <div>{this.renderMiddleSection()}</div> : '' }
          {this.state.questions.length > 0 && <div className={`answer-column ${this.state.is_correct !== '' ? 'not-active' : ''}`}>{this.renderAnswerButtons()}
          </div>}
        </>;
    return some;
  };

  renderQuestion = () => {
    const view = (this.state.questions.length - 1 >= this.props.match.params.id) ? (<Question question={this.state.questions[this.props.match.params.id]} />) : this.props.history.push('/score');
    return view;
  };

  noBack = () => {
    window.history.pushState(null, document.title, window.location.href);
    window.addEventListener('popstate', () => {
      window.history.pushState(null, document.title, window.location.href);
    });
  }

  render() {
    return (
      <div className="quiz-container">
        <div className="quiz">
          <div className="quiz-header">
            <div className="question-count">
              {this.noBack()}
              {Number(this.props.match.params.id) + 1} / {this.state.questions.length}
            </div>
            <div className="score">{this.state.score}pts</div>
          </div>
          <div className='quiz-body'>{this.renderonDOM()}</div>
          <div className='container'>{(this.state.count === 0 && this.state.questions.length) && this.runIt(this.props.match.params.id, false, 'time')}</div>
        </div>
        <Footer />
      </div>
    );
  }
}
