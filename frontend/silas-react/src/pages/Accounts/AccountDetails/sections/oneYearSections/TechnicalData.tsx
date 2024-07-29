import React from 'react';

import PieChart from '../../../../../components/Charts/PieChart';
import { Tabs, Tab } from '../../../../../components/Tabs';
import InlineCard from '../../../../../components/InlineCard';

const TechnicalData: React.FC = ({
  aalData,
techAdequacyData,
techRateValues,
lineRateValues,
}) => {
  return (
    <div className="w-full mb-4 border-b pb-4">
      <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
        Technical Data
      </h2>
      <div className="">
        <div className="bg-white">
          {aalData ? <InlineCard kpis={aalData} /> : null}
          {techAdequacyData ? <InlineCard kpis={techAdequacyData} /> : null}
          {techRateValues ? <InlineCard kpis={techRateValues} /> : null}
          {lineRateValues ? <InlineCard kpis={lineRateValues} /> : null}
        </div>
      </div>
    </div>
  );
};

export default TechnicalData;
