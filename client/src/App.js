import { useState, useEffect } from "react"
import { Route, Routes, useNavigate } from "react-router-dom"
import Navigation from "./components/Navigation/Navigation"
import Home from "./components/Home/Home"
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate()

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => {
          console.log(user) 
          setUser(user)
       });
        console.log(user)
        navigate('/')
      }
    });
  }, []);

  return (
    <>
      <div>
        <Navigation setUser={setUser} user={user} />
        <Routes>
          <Route path ="/" element = {<Home />}> </Route> 
        </Routes>
      </div>
    
    </>

  );
}

export default App;
