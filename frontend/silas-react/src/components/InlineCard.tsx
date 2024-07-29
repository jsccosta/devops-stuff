import React from 'react';
import { formatToDollar, formatToPercent, naivePercent } from '../utils/formatters';

const InlineCard: React.FC = ({ kpis }) => {
  return (
    <div className="flex bg-white justify-between p-4">
      {kpis.map((metric, index) => {
        const formattedValue = metric?.format === 'dollar' ? formatToDollar(metric.value) : metric?.format === 'perc' ? naivePercent(metric.value) : metric.value;
        return (
          <div key={index} id="metric" className="flex w-1/2 justify-between px-4">
            <h4 className="text-title-sm font-bold mr-4 text-black dark:text-white">
              {metric.label}
            </h4>
            <h4 className="text-title-sm text-black dark:text-white">
              {formattedValue}
            </h4>
          </div>
        );
      })}
    </div>
  );
};

export default InlineCard;
