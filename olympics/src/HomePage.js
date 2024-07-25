import React, { useState } from 'react';
import SearchBar from './SearchBar';
import Filters from './Filters';
import styles from './HomePage.module.css';
import olympicImage from './olympics_ring.png';
import mainFeature from './usain_bolt.jpeg';

const HomePage = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filters, setFilters] = useState({
    sport: '',
    country: ''
  });

  return (
    <div className={styles.homePage}>
      <div className={styles.banner}>
        <img src={olympicImage} alt="Olympic Games" className={styles.olympicImage} />
        {/* Add more images as needed */}
      </div>
      <div className={styles.searchArea}>
        <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
        <Filters filters={filters} setFilters={setFilters} />
      </div>
    </div>
  );
};

export default HomePage;