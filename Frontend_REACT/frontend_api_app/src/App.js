import React, { Component } from 'react';
import './App.css';
import { HashRouter as Router, Route, Switch} from 'react-router-dom';
import Status from './root/status';
import One_status from './root/one_status';
import Two_status from './root/two_status';
import One_book  from './root/book_one';
import Two_book  from './root/book_two';
import Search  from './root/search';



class App extends Component {
  nextPath(path) {

    this.props.history.push(path);
  }
  render(){
    return (
      <div className="App-header">
        
        <Router>
          <Switch>
            <Route exact path="/" component = {Search} />
            <Route exact path="/flights" component = {Status} />
            <Route exact path="/flights/one/status" component = {One_status} />
            <Route exact path="/flights/two/status" component = {Two_status} />
            <Route exact path="/flights/one/book" component = {One_book} />
            <Route exact path="/flights/two/book" component = {Two_book} />
          </Switch>
          
        
        </Router>

      </div>
    );
  }
}

export default App;