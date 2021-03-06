import React, { useState } from 'react';
import {
  Button, Modal, ModalHeader, ModalBody,
} from 'reactstrap';
import sustaingame from '../../images/sustaingame.png';

const NoActiveEvents = (props) => {
  const {
    buttonLabel,
    className,
  } = props;

  const [modal, setModal] = useState(false);

  const toggle = () => setModal(!modal);

  // add custom close button icon here
  const closeBtn = <button className="close" onClick={toggle}>&times;</button>;

  return (
    <div className="modal-container">
      <Button className="btn-dark mb-4" color="info" onClick={toggle}>{buttonLabel}</Button>
      <Modal isOpen={modal} toggle={toggle} className={className}>
        <ModalHeader toggle={toggle} close={closeBtn}></ModalHeader>
        <ModalBody className="mx-4">
          <img src={sustaingame} alt="sustain game" className="sustaingame-img"/>
          <h1>No Active Events</h1>
          <p className="container">Currently there are not any active events happening. Check out "How to Play" to be prepared for when the next challenge is available</p>

          <p className="container">In the meantime, checkout our <a href="https://urbangreenlab.org/">website</a> for more details about what we do and who we are.</p>
        </ModalBody>
      </Modal>
    </div>
  );
};

export default NoActiveEvents;
