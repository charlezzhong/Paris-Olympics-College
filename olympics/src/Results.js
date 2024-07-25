import React from 'react';
import AthleteCard from './AthleteCard';
import styles from './Results.module.css';

const Results = ({ athletes }) => {
  return (
    <div className={styles.resultsContainer}>
      {athletes.map((athlete) => (
        <AthleteCard key={athlete.id} athlete={athlete} />
      ))}
    </div>
  );
};

export default Results;