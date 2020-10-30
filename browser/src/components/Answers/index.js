import React from 'react';
import { Button } from 'reactstrap';

const Answer = (props) => props.a.map((a, i) => <Button
    className={`answer-btn ${a.is_correct ? 'c' : 'i'}`}
    outline color="secondary"
    id={`button-${i}`}
    key={i}
    onClick={() => props.click(props.id, a.is_correct, i)}
    // disabled={props.disabled}
  >
    {a.answer}
  </Button>);

export default Answer;
