import React, { useState } from 'react';
import {
  Button, Modal, ModalHeader, ModalBody,
} from 'reactstrap';
import sustaingame from '../../images/sustaingame.png';
import number1 from '../../images/number1.png';
import number2 from '../../images/number2.png';

const GameModal = (props) => {
  const {
    buttonLabel,
    className,
  } = props;

  const [modal, setModal] = useState(false);

  const toggle = () => setModal(!modal);

  // add custom close button icon here
  const closeBtn = <button className="close" onClick={toggle}>&times;</button>;

  return (
    <div>
      <Button className="btn-transparent" color="info" onClick={toggle}>{buttonLabel}</Button>
      <Modal isOpen={modal} toggle={toggle} className={className}>
        <ModalHeader toggle={toggle} close={closeBtn}></ModalHeader>
        <ModalBody>
          <img src={sustaingame} alt="sustain game" className="sustaingame-img"/>
          <h1>How to Play</h1>
          <img src={number1} alt="1" className="modal-number"/>

          <p style={{ textAlign: 'center' }}>Players will have 10 seconds to answer each question. The faster you answer the more points you’ll receive!</p>

          <img src={number2} alt="2" className="modal-number"/>

          <p style={{ textAlign: 'center' }}>Once all questions have been answered, players will be asked to add their initials to the leaderboard and winner information will be displayed on the leaderboard and will show players personal results and rank.</p>
        </ModalBody>
      </Modal>
    </div>
  );
};

export default GameModal;
