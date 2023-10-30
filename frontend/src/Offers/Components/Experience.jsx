export const OfferExperience = ({ offer }) => {
  const experienceLevels = offer.experience_level || [];

  return (
    <div className="offer-exp">
      <span>
        {experienceLevels
          .map((experienceLevel) => experienceLevel.name)
          .join(", ")}
      </span>
    </div>
  );
};