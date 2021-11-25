const React = require('react')
import Try from './Try'

function getNumbers() {

}

class NumberBaseball extends React.Component {
    state = {
        result: '',
        value: '',
        answer: getNumbers(),
        tries : []
 
    }

    onSubmit = () => {

    }

    onChangeInput = () => {

    }

    fruits = [
        {fruit:'사과', taste:'맛있'},
        {fruit:'vheh', taste:'심'},
    ]

    render() {
        return  (
        <>
            <h1>{this.state.result}</h1>
            <form onSubmit={this.onSubmit}>
                <input maxLength={4} value={this.state.value} onChange={this.onChangeInput} />
            </form>
            <div>시도 : {this.state.tries.length}</div>
            <ul>
                {this.fruits.map((v,i)=> {
                    return (
                        <Try value={v} index={i}/>
                    )
                })}
               
            </ul>
        </>
        )
    }
}

export default NumberBaseball