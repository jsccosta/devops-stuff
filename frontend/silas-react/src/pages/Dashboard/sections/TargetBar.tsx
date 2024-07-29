import React from 'react';

import ProgressBar from '../../../components/ProgressBar';

const TargetBar: React.FC = ({ label, targetValue }) => {
  return (
    <div
      id="written_premium_target"
      className="relative w-full my-4 border-b pb-4"
    >
      <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
        {label}
      </h2>
      <ProgressBar percentage={targetValue} />
    </div>
  );
};

export default TargetBar;
