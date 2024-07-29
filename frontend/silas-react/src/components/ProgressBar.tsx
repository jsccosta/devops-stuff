import React from 'react';

const ProgressBar: React.FC = ({ percentage }) => {
  return (
    <div className="flex flex-col relative h-12 bg-silas-dark text-white rounded-md flex items-center">
      <div
        className="h-12 left-0 absolute bg-silas-light rounded-md"
        style={{ width: `${percentage}%` }}
      >
        <div className="absolute right-2 top-1/2 transform -translate-y-1/2 text-xl font-bold text-silas-contrast">
          {percentage}%
        </div>
      </div>
    </div>
  );
};

export default ProgressBar;
