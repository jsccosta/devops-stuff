import React from 'react';

import PieChart from '../../../../../components/Charts/PieChart';
import InlineCard from '../../../../../components/InlineCard';

const PropertyDamage: React.FC = ({
  propertyDamageData,
  deductibleData,
  claimsChartData,
  damagesBreakdown,
}) => {
  return (
    <div className="w-full mb-4 border-b pb-4">
      <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
        Property Damage
      </h2>
      <div className=" mb-4">
        <div className="bg-white">
          {propertyDamageData ? <InlineCard kpis={propertyDamageData} /> : null}
          {deductibleData ? <InlineCard kpis={deductibleData} /> : null}
        </div>
        <div className="grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-4 xl:grid-cols-3 2xl:gap-7.5 my-4">
          {claimsChartData ? (
            claimsChartData.map((claimsData, index) => {
              return (
                <PieChart
                  key={index}
                  title={claimsData.title}
                  data={claimsData.data}
                  labels={claimsData.labels}
                />
              );
            })
          ) : (
            <div>Loading...</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default PropertyDamage;
