import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import About from './About';
import Home from './Home';
import './App.css';
// import Profile from './components/Profile';
import Profiles from './components/Profiles';

const App = () => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">홈</Link>
        </li>
        <li>
          <Link to="/about">소개</Link>
        </li>
        {/* <li>
          <Link to="/profile/Dean">Dean 프로필</Link>
        </li>
        <li>
          <Link to="/profile/kangho">캉호우 프로필</Link>
        </li> */}
        <li>
          <Link to="/profiles">프로필</Link>
        </li>
      </ul>
      <hr />
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/about" element={<About/>} />
        {/* <Route path="/info" element={<About/>} /> */}
        {/* <Route path="/profile/:username" element={<Profile />} /> */}
        <Route path="/profiles" element={<Profiles/>} />
      </Routes>
    </div>
  );
};


export default App;
