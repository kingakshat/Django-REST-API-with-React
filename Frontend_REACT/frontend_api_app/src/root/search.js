import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


class Status extends Component {

  nextPath(path) {
    this.props.history.push(path);
  }  
  render(){

    
        return(
        
        <header className='App'>
             <div style={{ width: '100%' }} className='All'>
                <h1 class='size'>WELCOME TO <strong>BOOK MY TICKET</strong></h1>
<br/><br/>
                <h4>Click to Search for Available Flights</h4>
<br/>
                <Button onClick={() => this.nextPath('/flights') }>
                        <h4>SEARCH FOR FLIGHTS</h4>
                </Button>
            <p class="End">Coded with &#128151; By AKSHAT</p>
            </div>

        </header>
        
        );
    
  }

}  

export default Status;