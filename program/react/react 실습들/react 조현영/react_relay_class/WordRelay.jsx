const React = require('react')

class WordRelay extends React.Component {
    state = {
        result: '',
        word: '제로초',
        value: '',
    }

    onSubmitForm = (e) => {
        e.preventDefault()
        if(this.state.word[this.state.word.length -1] === this.state.value[0]) {
            this.setState({
                result: 'O',
                word: this.state.value,
                value: ''
            })
            this.input.focus()
        } else {
            this.setState({
                result: '땡',
                value: ''
            })
            this.input.focus()
        }
    }

    onChangeInput = (e) => {
        this.setState({value: e.target.value})
    }

    input

    onRefInput = (c) => {
        this.input = c
    }


    render() {
        return  (
        <>
            <div>
                {this.state.word}
            </div>
            <form onSubmit={this.onSubmitForm}>
                <input ref={this.onRefInput} value = {this.state.value} onChange={this.onChangeInput} />
                <button>button</button>
            </form>
            <div>{this.state.result}</div>

        </>
        )
    }
}

module.exports = WordRelay