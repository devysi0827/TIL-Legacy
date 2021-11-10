import React, { Component } from 'react'
import PhoneInfo from './PhoneInfo'

export default class PhoneInfoList extends Component {
    render() {


        const {data, onRemove} = this.props

        if (!data) return null
        const list =data.map(
            info=> <PhoneInfo onRemove={ onRemove} info={info} key={info.id} />)
        return (
            <div>
                {list}
            </div>
        )
    }
}
