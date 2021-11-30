const React = require('react')
const { useState,useRef } = React 

const WordRelay = () => {
    const [word,setWord] = useState('제로초')
    const [value,setvalue] = useState('')
    const [result,setResult] = useState('')
    const inputRef = useRef(null)

    
    const onSubmitForm = (e) => {
        e.preventDefault()
        if(word[word.length -1] === value[0]) {
            setResult('O')
            setWord(value)
            setvalue('')
            inputRef.current.focus()
        } else {
            setResult('x')
            setvalue('')
            inputRef.current.focus()
        }
    }

    const onChangeInput = (e) => {
        setvalue(e.target.value)
    }


    return  (
    <>
        <div>{word}</div>
        <form onSubmit={onSubmitForm}>
            <input ref={inputRef} value = {value} onChange={onChangeInput} />
            <button>button</button>
        </form>
        <div>{result}</div>

    </>
    )
}


module.exports = WordRelay