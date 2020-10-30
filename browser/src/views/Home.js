import React, { Component } from 'react';
import {
  Button, Form, FormGroup, Label, Input,
} from 'reactstrap';
import UglLogo from '../images/UglLogo.png';
import floatingBoxes from '../images/floatingBoxes.png';

export default class Home extends Component {
  state = {
    fname: '',
    lname: '',
    email: '',
    zip_code: '',
  }

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value,
    });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem('user', JSON.stringify(this.state));
    this.props.history.push('/countdown');
  }

  render() {
    return (
      <div className="home">
        <img src={floatingBoxes} alt="" className="bg-img"/>

        <div className="home-form">
          <h1>Before we begin</h1>
          <Form onSubmit={this.handleSubmit} >
            <FormGroup>
              <Label for="fname">First Name <span className="form-required">*</span></Label>
              <Input onChange={this.handleChange} type="text" name="fname" id="fname" required/>
            </FormGroup>
            <FormGroup>
              <Label for="lname">Last Name <span className="form-required">*</span></Label>
              <Input onChange={this.handleChange} type="text" name="lname" id="lname" required/>
            </FormGroup>
            <FormGroup>
              <Label for="email">Email <span className="form-required">*</span></Label>
              <Input onChange={this.handleChange} type="email" name="email" id="email" required/>
            </FormGroup>
            <FormGroup>
              <Label for="zip_code">Zip Code <span className="form-required">*</span></Label>
              <Input onChange={this.handleChange} type="text" pattern="[0-9]*" name="zip_code" id="zip_code" maxLength="5" required/>
            </FormGroup>
            <Button className='btn btn-dark'>Get Ready</Button>
          </Form>
        </div>
        <p>brought to you by</p>
        <img src={UglLogo} alt="urban green lab" className="ugl-logo"/>
      </div>
    );
  }
}
