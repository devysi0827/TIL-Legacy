import React, {Component} from 'react'

class Try extends Component {
    render () {
        return (
           <li>
               <b>{this.props.value.fruit}</b> - {this.props.index}
               <div>ddd</div>
               <div>ccc</div>
           </li>
        )
    }
}

export default Try