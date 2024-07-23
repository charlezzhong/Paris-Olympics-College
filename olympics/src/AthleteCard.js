import React from 'react';
import { Link } from 'react-router-dom';

const AthleteCard = ({ athlete }) => {
  return (
    <div>
      <h2>{athlete.name}</h2>
      <p>{athlete.sport}</p>
      <p>{athlete.college}</p>
      <Link to={`/athlete/${athlete.id}`}>View Details</Link>
    </div>
  );
};

export default AthleteCard;