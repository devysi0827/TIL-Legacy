// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  // Link
} from "react-router-dom"

import LandingPage from './components/views/LandingPage/Sections/LandingPage';
import RegisterPage from './components/views/RegisterPage/RegisterPage'
import LoginPage from './components/views/LoginPage/LoginPage'
import Auth from './hoc/auth'
import NavBar from './components/views/NavBar/NavBar';
import Footer from './components/views/Footer/Footer'
// import Spinner from './homeviews/loadingspinner/Spinner';



function App() {
  return (
    <Router>
    <div>
      <NavBar/>
      {/* <Spinner /> */}
      <Switch>
        <Route exact path="/" component={Auth(LandingPage, null)} />
        <Route exact path="/Register" component={Auth(RegisterPage, false)} />
        <Route exact path="/login" component={Auth(LoginPage, false)} />
      </Switch>

      <hr/>
      <Footer/>
    </div>
  </Router>

  );
}

export default App;
