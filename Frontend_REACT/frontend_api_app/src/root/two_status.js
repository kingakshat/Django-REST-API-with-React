import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';






class Two_status extends Component {
  constructor(props){
    super(props);
    this.state = {
      item: [ ],
      isLoaded: false
    } 
  }
 
  componentDidMount() {
    fetch("http://127.0.0.1:8000/two/status")
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
                <ul class="list-group list-group-flush">

                     {items.map((items, index) => {
                          return index <= 0 ? <li class="list-group-item">Flight name :- { items.f_name } </li> : undefined
                        })}
                    {items.map((items, index) => {
                          return index <= 0 ? <li class="list-group-item"> Source and Destination :- { items.s_n_d }</li> : undefined
                        })}
                </ul>
               
<br/><br/>

                <table class="table table-sm table-dark">
                <thead class="thead-dark">
                <tr>
                        <td colspan="15">Available Seats</td>
                </tr>
                </thead>
                <tbody>    
                <tr>
               
                    {items.map((items, index) => { return index <= 14 ? <td> { items.seat_name} </td> : undefined })}
               
                </tr>
                <tr>
               
                  {items.map((items, index) => { return index >= 15 ? <td> { items.seat_name } </td> : undefined })}
               
                </tr>
                </tbody>
                </table>

                <Button onClick={() => this.nextPath('/flights/two/book') }>
                  BOOK YOUR TICKET
                </Button>
                </div>
            </header>    
        );
    }
  }

}  

export default Two_status;



//* {items.map(items => (
//                         <li class="list-group-item"  key={ items.id }> 
//                             { items.seat_name }
//                         </li>
//                         ))}