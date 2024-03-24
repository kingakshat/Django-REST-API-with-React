import React, { Component } from 'react';
import { jsPDF } from "jspdf";
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';

class Two_book extends Component {
    constructor(props){
      super(props);
      this.state = {
        seat_no: '',
        booking_name: '',
        items: [ ],
        isLoaded: false,
        //   'timeframes': this.state.timeframes,
      } 
    }


    jsPDFGenerator = (result) =>{

      var doc = new jsPDF('l','pt', 'a4');
      doc.setFont('Helvetica', "bold");
      doc.setFontSize('30');
      doc.text(130,100, "THANK YOU FOR USING BOOK MY TICKET")
      doc.setFontSize('22');
      doc.text(120,200, "Flight Name....................:- " +result[0])
      doc.text(120,250,"Source & Destination....:- " +result[1])
      doc.text(120,300,"Seat Numbers................:- " +result[2])
      doc.text(120,350,"Booking Name...............:- " +result[3])
      doc.text(120,400,"Booking ID.....................:- " +result[4])
      doc.text(120,450,"Booking Time................:- " +result[5])

      doc.save('TICKET.pdf')
    }

    handleSubmit(event){
        // event.preventDefault()
        // console.log(event)
        let setResp = this;
        fetch("http://127.0.0.1:8000/two/book",{
          method:"POST",
          headers:{
            'Accept':'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
           
              'seat_no' : this.state.seat_no,
              'booking_name' : this.state.booking_name,
            
          })
          
        })
            .then(function(response) {
            return response.json();
            })
            .then(function(response) {
            setResp.setState({ 
              responseData: response,
              isLoaded: true,
              items: response, 
            });
            
            })
      
    }
    render() {     
       
       var dis = 'None';
       var { items,  isLoaded } = this.state
       const result = Object.values(items);
       console.log(isLoaded)
       if(isLoaded) { dis = 'Inline'};
       console.log(dis,result)
       return ( 
             <header className='App-header'>
             <div className='All'>
                Seat Numbers
                <input value={this.state.name} className="form-control email" name='seat_no' onChange={(text) => { this.setState({ seat_no: text.target.value }) }} />
                
                Booking Name
                <input value={this.state.name} className="form-control email" name='booking_name' onChange={(text) => { this.setState({ booking_name: text.target.value }) }} />
<br/><br/>
                <Button onClick={() => this.handleSubmit() }>
                  BOOK MY TICKET
                </Button>
<br/><br/>
                <div style={{ display: dis }}>
                   <h3>Your Ticket is booked</h3>
                   <table class="table table-striped table-dark">
                   <thead class="thead-dark">
                   <tr>
                      <th scope="col">Flight</th>
                      <th scope="col">From - To</th>
                      <th scope="col">Seat</th>
                      <th scope="col">Name</th>
                      <th scope="col">Booking ID</th>
                      <th scope="col">Bookig Time</th>
                   </tr>
                   </thead>
                   <tbody>
                  <tr>
                      <td>{ result[0] }</td>
                      <td>{ result[1] }</td>
                      <td>{ result[2] }</td>
                      <td>{ result[3] } </td>
                      <td>{ result[4] } </td>
                      <td>{ result[5] } </td>
                  </tr>
                  </tbody> 
                  </table>
<br/>
                  <Button onClick={() => this.jsPDFGenerator(result) }>
                    DOWNLOD TICKET
                  </Button>
               </div>
       </div>
       </header>
    )
        
    }
}

export default Two_book;


