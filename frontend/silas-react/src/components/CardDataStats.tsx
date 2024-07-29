import React from 'react';
import { BsGraphUpArrow } from 'react-icons/bs';

interface CardDataStatsProps {
  title: string;
  total: string | number;
  formatType?: string;
}

const formatValue = (value: string | number, formatType?: string): string => {
  if (!formatType) return value.toString();

  let formatter: Intl.NumberFormat;

  if (formatType === 'dollar') {
    formatter = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    });
    return formatter.format(value);
  } else if (formatType === 'percentage') {
    return `${value.toLocaleString('en-US', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    })}%`;
  }
};

const CardDataStats: React.FC<CardDataStatsProps> = ({
  title,
  total,
  formatType,
}) => {
  return (
    <div className="rounded-sm border border-stroke bg-white py-2 px-3 shadow-default dark:border-strokedark dark:bg-boxdark">
      <div className="flex items-end justify-between">
        <div className="flex items-center">
          {title === 'Rate Change' ? (
            <BsGraphUpArrow color="green" size="45px" />
          ) : null}
          <div className="ml-3">
            <span className="text-lg font-medium">{title}</span>
            <h4 className="text-title-md text-black dark:text-white">
              {formatValue(total, formatType)}
            </h4>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CardDataStats;
