import React from 'react';
import styles from './Filters.module.css';

const Filters = ({ filters, setFilters }) => {
  const handleChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className={styles.filterContainer}>
      <select name="sport" value={filters.sport} onChange={handleChange} className={styles.filterSelect}>
        <option value="">Select Sport</option>
        <option value="basketball">Basketball</option>
        <option value="swimming">Swimming</option>
        <option value="track">Track</option>
        <option value="gymnastics">Gymnastics</option>
        {/* Add more sports as needed */}
      </select>
      <select name="country" value={filters.country} onChange={handleChange} className={styles.filterSelect}>
        <option value="">Select Country</option>
        <option value="USA">USA</option>
        <option value="Canada">Canada</option>
        {/* Add more countries as needed */}
      </select>
    </div>
  );
};

export default Filters;