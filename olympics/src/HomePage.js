import React, { useState } from 'react';
import SearchBar from './SearchBar';
import Filters from './Filters';
import Results from './Results';

const HomePage = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filters, setFilters] = useState({
    sport: '',
    country: ''
  });
  const [athletes, setAthletes] = useState([]);

  const handleSearch = async () => {
    // Fetch data from backend based on searchTerm and filters
    // Update athletes state with fetched data
  };

  return (
    <div>
      <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      <Filters filters={filters} setFilters={setFilters} />
      <button onClick={handleSearch}>Search</button>
      <Results athletes={athletes} />
    </div>
  );
};

export default HomePage;