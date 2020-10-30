import React, { Component } from 'react';
import { Alert } from 'reactstrap';
import getActiveEvent from '../data/getActiveEvent';
import Question from '../components/Question';
import Answers from '../components/Answers';

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
      this.setState({
        questions: resp[0].questions,
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
        const bonusPoints = this.state.count * 100;
        const score = qpoints ? bonusPoints + this.state.questions[id].value : 0;
        this.setState({
          score: this.state.score + score,
          is_correct: qpoints,
          current_value: this.state.questions[id].value,
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
      <div className='correct-emoji'>EMOJI</div>
      <div>CORRECT {this.state.current_value}pts! <br /> BONUS +{this.state.current_bp} for fast answer</div>
    </Alert>;
    } else {
      view = <Alert className='score-info'>
      <div className='correct-emoji'>EMOJI</div>
      <div>Wrong Answer <br /> 0pts</div>
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
          {this.state.questions.length > 0 ? this.renderQuestion() : 'Loading'}
          <div className='container'>{this.renderMiddleSection()}</div>
          {this.state.questions.length > 0 && <div className='answer-column'>{this.renderAnswerButtons()}
          </div>}
        </>;
    return some;
  };

  renderQuestion = () => {
    const view = (this.state.questions.length - 1 >= this.props.match.params.id) ? (<Question question={this.state.questions[this.props.match.params.id]} />) : this.props.history.push('/score');
    return view;
  };

  render() {
    return (
      <div>
        <div className="quiz-header">
        <div>{Number(this.props.match.params.id) + 1} / {this.state.questions.length}</div>
        <div>{this.state.score}pts</div>
        </div>
        <div className='container'>{this.renderonDOM()}</div>
        <div className='container'>{(this.state.count === 0 && this.state.questions.length) && this.runIt(this.props.match.params.id, false, 'time')}</div>
      </div>
    );
  }
}
