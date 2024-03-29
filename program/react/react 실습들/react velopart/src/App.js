import React, { Component } from 'react';
import './App.css';
import PhoneForm from './components/PhoneForm';
// import PhoneInfo from './components/PhoneInfo';
import PhoneInfoList from './components/PhoneInfoList';

class App extends Component {
  
  id= 0
  state= {
    information: []
  }
  
  handleCreate = (data) => {
    this.setState({
      information: this.state.information.concat({
        ...data,
        id: this.id++
      })
    })
  }

  handleRemove = (id) => {
    const {information} = this.state;
    this.setState({
      information: information.filter(info => info.id !== id)
    })
  }

  render() {
    return (
      <div >
        <PhoneForm onCreate={this.handleCreate} />
        <PhoneInfoList 
          data={this.state.information}
          onRemove={this.handleRemove}
          />
      </div>
    );
  }
}

export default App;
