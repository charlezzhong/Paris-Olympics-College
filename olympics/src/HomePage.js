import React, { useState } from 'react';
import SearchBar from './SearchBar';
import Filters from './Filters';
import Results from './Results';
import styles from './HomePage.module.css';
import olympicImage from './olympics_ring.png';
import mainFeature from './usain_bolt.jpeg';

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
        <img src={olympicImage} alt="Olympic Games" className={styles.olympicImage} />
        <h1 className={styles.title}>NCAA Athletes Competing in Paris Olympics</h1>
      </div>
      <div className={styles.featuredAthlete}>
        <img src={mainFeature} alt="Featured Athlete" className={styles.featuredImage} />
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