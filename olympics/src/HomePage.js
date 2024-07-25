import React, { useState } from 'react';
import SearchBar from './SearchBar';
import Filters from './Filters';
import Results from './Results';
import styles from './HomePage.module.css';
import boltImage from './main.png'; // Ensure this import points to the correct file path

const HomePage = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filters, setFilters] = useState({
    school: '',
    sport: '',
    olympicSport: '',
    country: '',
    conference: '',
    division: ''
  });

  return (
    <div className={styles.homePage}>
      <div className={styles.banner}>
        <img src={boltImage} alt="Usain Bolt Celebration" className={styles.bannerImage} />
        <h1 className={styles.bannerTitle}>NCAA Athletes Competing in Paris Olympics</h1>
      </div>
      <div className={styles.searchAndFilters}>
        <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
        <Filters filters={filters} setFilters={setFilters} />
      </div>
      <Results filters={filters} searchTerm={searchTerm} />
    </div>
  );
};

export default HomePage;
