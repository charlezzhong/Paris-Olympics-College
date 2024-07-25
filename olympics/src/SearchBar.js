import React from 'react';
import styles from './SearchBar.module.css';

const SearchBar = ({ searchTerm, setSearchTerm }) => {
  return (
    <input
      type="text"
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      placeholder="Enter college name"
      className={styles.searchInput}
    />
  );
};

export default SearchBar;