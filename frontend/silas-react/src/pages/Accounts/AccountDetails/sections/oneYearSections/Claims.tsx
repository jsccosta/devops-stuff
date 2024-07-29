import React from 'react';

import InlineCard from '../../../../../components/InlineCard';

const Claims: React.FC = ({
  gwpNwpValues,
  policyLimit,
  rateValues,
  feesAndBrokerage,
}) => {
  return (
    <div id="claims" className="relative w-full my-4 border-b pb-4">
      <div className="bg-white mb-4">
        {gwpNwpValues ? <InlineCard kpis={gwpNwpValues} /> : null}
        {policyLimit ? <InlineCard kpis={policyLimit} /> : null}
        {rateValues ? <InlineCard kpis={rateValues} /> : null}
        {feesAndBrokerage ? <InlineCard kpis={feesAndBrokerage} /> : null}
      </div>
    </div>
  );
};

export default Claims;
