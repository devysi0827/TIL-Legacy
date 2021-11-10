import React, { Component } from 'react'

export default class PhoneInfo extends Component {
    handleRemove =  () => {
        const {info, onRemove} = this.props
        onRemove(info.id)
    }
    render() {
        const {name, phone} = this.props.info
        return (
            <div>
                <div>{name}</div>
                <div>{phone}</div>
                <button onClick={this.handleRemove}>삭제</button>
                {/* <div>{id}</div> */}

            </div>
        )
    }
}
