import React, { useState } from 'react';
import {
  Button, Modal, ModalHeader, ModalBody,
} from 'reactstrap';

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
      <Button color="info" onClick={toggle}>{buttonLabel}</Button>
      <Modal isOpen={modal} toggle={toggle} className={className}>
        <ModalHeader toggle={toggle} close={closeBtn}>How to play</ModalHeader>
        <ModalBody>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </ModalBody>
      </Modal>
    </div>
  );
};

export default GameModal;