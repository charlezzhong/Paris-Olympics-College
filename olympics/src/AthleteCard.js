import React from 'react';
import { Link } from 'react-router-dom';
import styles from './AthleteCard.module.css';

const AthleteCard = ({ athlete }) => {
  return (
    <div className={styles.card}>
      <h2>{athlete.name}</h2>
      <p>{athlete.sport}</p>
      <p>{athlete.college}</p>
      <Link to={`/athlete/${athlete.id}`} className={styles.detailsLink}>View Details</Link>
    </div>
  );
};

export default AthleteCard;