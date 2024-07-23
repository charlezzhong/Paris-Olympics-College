import React, { useEffect, useState } from 'react';

const AthleteDetails = ({ match }) => {
  const [athlete, setAthlete] = useState(null);

  useEffect(() => {
    const fetchAthleteDetails = async () => {
      const response = await fetch(`/api/athletes/${match.params.id}`);
      const data = await response.json();
      setAthlete(data);
    };

    fetchAthleteDetails();
  }, [match.params.id]);

  if (!athlete) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{athlete.name}</h1>
      <p>Sport: {athlete.sport}</p>
      <p>College: {athlete.college}</p>
      <p>Country: {athlete.country}</p>
      {/* Add more athlete details as needed */}
    </div>
  );
};

export default AthleteDetails;