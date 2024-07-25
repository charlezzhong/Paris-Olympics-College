import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage';
import AthleteDetails from './AthleteDetails';
import './App.css';

const App = () => {
  console.log('App is rendering');
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route path="/athlete/:id" element={<AthleteDetails />} />
      </Routes>
    </Router>
  );
};

export default App;
