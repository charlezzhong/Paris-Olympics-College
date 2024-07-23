import React from 'react';
import AthleteCard from './AthleteCard';

const Results = ({ athletes }) => {
  return (
    <div>
      {athletes.map((athlete) => (
        <AthleteCard key={athlete.id} athlete={athlete} />
      ))}
    </div>
  );
};

export default Results;