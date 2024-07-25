import React from 'react';
import AthleteCard from './AthleteCard';
import styles from './Results.module.css';

const Results = ({ athletes }) => {
  // Check if athletes is an array and has elements before trying to map over it
  if (!Array.isArray(athletes) || athletes.length === 0) {
    return <div className={styles.resultsContainer}>No athletes found</div>;
  }

  return (
    <div className={styles.resultsContainer}>
      {athletes.map((athlete) => (
        <AthleteCard key={athlete.id} athlete={athlete} />
      ))}
    </div>
  );
};

export default Results;