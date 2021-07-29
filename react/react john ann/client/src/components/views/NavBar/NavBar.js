

import React from 'react'
import { Navbar, Container, Nav} from 'react-bootstrap'
import imageA from './logo.png'

function NavBar() {
    return (
        <div>
            <Navbar bg="dark" variant="dark">
                <Container>
                <Navbar.Brand href="#home">
                    <img
                    alt="logo"
                    src= {imageA}
                    width="30"
                    height="30"
                    className="d-inline-block align-top"
                    />{' '}
                </Navbar.Brand>
                
        
                        <div class="justify-content-center">
                            <button style={{background: "white"}} ><Nav.Link style={{color: "black"}} href="/register">회원가입</Nav.Link></button>
                            <button style={{background: "blue"}} ><Nav.Link style={{color: "black"}} href="/login">로그인</Nav.Link></button>
                        </div>
                </Container>
            </Navbar>
        </div>
    )
}



export default NavBar
