import React from 'react';

import { formatToDollar, naivePercent } from '../utils/formatters';

const StackedDataCard: React.FC = ({kpis}) => {

  return (
    <div className="mb-4 rounded-sm border border-stroke bg-white py-2 px-3 shadow-default dark:border-strokedark dark:bg-boxdark">
      <div className="flex items-end justify-between h-full">
        <div className="flex flex-col items-left w-full h-full justify-between">
          {kpis.map((kpi, index) => {
            const formattedValue = kpi?.format === 'dollar' ? formatToDollar(kpi.value) : kpi?.format === 'perc' ? naivePercent(kpi.value) : kpi.value;
            return (
              <div key={index} className="flex items-left justify-between ml-3 py-2 ">
                <div className="flex flex-col">
                  <span className="text-lg font-medium mr-4">{kpi.label}</span>
                  {kpi.subtitle ? (
                    <span className="text-sm font-medium mr-4">
                      {kpi.subtitle}
                    </span>
                  ) : null}
                </div>
                <h4 className="text-title-md text-black dark:text-white">
                  {formattedValue}
                </h4>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default StackedDataCard;
