import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


class Status extends Component {
  constructor(props){
    super(props);
    this.state = {
      item: [ ],
      isLoaded: false
    } 
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/status')
       .then(res => res.json())
       .then(json => {
           this.setState({
             isLoaded: true,
             items: json,
           })
       })
  }
  nextPath(path) {
    this.props.history.push(path);
  }
  
 

  


  render(){

    var { isLoaded, items } = this.state
    
    if(!isLoaded){
        return(
             <header class='App-header'>Loading</header>    
        );
    }
    else {
        return(
          
         <header class='App-header'>
         <div className='All'>
            <table class="table table-striped table-dark">
            <thead>
            <tr>
                <th>Flight Name</th>
                <th>Source and Destination</th>
                <th>Available seats</th>
                <th>Check</th>
            </tr>
            </thead>
            <tbody>    
            <tr>
               
                {items.map((items, index) => { return index === 0 ? <td> { items.f_name } </td> : undefined })}
                {items.map((items, index) => { return index === 0 ? <td> { items.s_n_d } </td> : undefined })}
                {items.map((items, index) => { return index === 0 ? <td> { items.ava_seat } </td> : undefined })}
                <td>
                    <Button onClick={() => this.nextPath('/flights/one/status') }>
                        CHECK SEATS AVAILABLE FOR ONE
                    </Button>
                </td> 
            </tr>
            </tbody>
            <tbody>
            <tr>
               
                {items.map((items, index) => { return index === 1 ? <td> { items.f_name } </td> : undefined })}
                {items.map((items, index) => { return index === 1 ? <td> { items.s_n_d } </td> : undefined })}
                {items.map((items, index) => { return index === 1 ? <td> { items.ava_seat } </td> : undefined })}
                <td>
                    <Button onClick={() => this.nextPath('/flights/two/status') }>
                        CHECK SEATS AVAILABLE FOR ONE
                    </Button>
                </td> 
            </tr>
            </tbody>
            </table>    
          </div>  
        </header>    
        );
    }
  }

}  

export default Status;


