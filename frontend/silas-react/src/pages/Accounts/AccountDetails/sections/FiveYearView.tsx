import React, { useEffect, useState } from 'react';

import { useParams } from 'react-router-dom';

import InlineCard from '../../../../components/InlineCard';
import GrossWrittenPremium from './fiveYearSections/GrossWrittenPremium';
import RateChange from './fiveYearSections/RateChange';
import TotalInsuredValue from './fiveYearSections/TotalInsuredValue';
import GrossClaims from './fiveYearSections/GrossClaims';

import { metricsLabels } from '../../../../metricsDescriptions';

// import Table from '../../../components/Tables/Table';

// import { convertRotatedData, convertTableHeaders, rotateData } from './helpers';


function calculateYoYChange(values: number[]) {
  const percentageChanges = [];
  for (let i = 1; i < values.length; i++) {
    const previousValue = values[i - 1];
    const currentValue = values[i];
    const percentageChange =
      ((currentValue - previousValue) / previousValue) * 100;
    percentageChanges.push(percentageChange);
  }
  return percentageChanges;
}

const FiveYearView: React.FC = ({ viewDetailsTable }) => {
  const [tableHeaders, setTableHeaders] = useState(null);
  const [tableData, setTableData] = useState(null);

  const [yearsRange, setYearsRange] = useState(null);
  const [gwpSeries, setGwpSeries] = useState(null);
  const [gwpYoYChange, setGwpYoYChange] = useState(null);

  const [rateChangeSeries, setRateSeries] = useState(null);
  const [rateChangeYoYChange, setRateYoYChange] = useState(null);

  const [tivChangeSeries, setTivChangeSeries] = useState(null);
  const [tivChangeYoYChange, setTivChangeYoYChange] = useState(null);

  const [claimsSeries, setClaimsSeries] = useState(null);

  const [gwpNwpValue, setGwpNwpValues] = useState(null);
  const [damageInterruptionValues, setDamageInterruptionValues] =
    useState(null);
  const [aopDeductibleValues, setAopDeductibleValues] = useState(null);


  const { accountId } = useParams();
  // const accountId = 1;

  const gwpChartOptions = {
    xaxis: {
      categories: yearsRange,
    },
  };

  useEffect(() => {
    const apiUrl = `/api/v1/new_metrics_global?company_id=${accountId}`;

    fetch(apiUrl)
      .then((response) => {
        // Check if the response is successful
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Parse the response as JSON
        return response.json();
      })
      .then((data) => {
        const groupedMetrics = data.company_metrics.reduce((acc, item) => {
          Object.entries(item).forEach(([key, value]) => {
            acc[key] = acc[key] || [];
            acc[key].push(value);
          });
          return acc;
        }, {});

        setYearsRange(groupedMetrics.year);
        setGwpSeries([
          {
            name: metricsLabels['gwp'],
            data: groupedMetrics.gwp,
          },
        ]);
        setGwpYoYChange(calculateYoYChange(groupedMetrics.gwp));
        setRateSeries([
          {
            name: metricsLabels['rate_change'],
            data: groupedMetrics.rate_change,
          },
        ]);
        setRateYoYChange(calculateYoYChange(groupedMetrics.rate_change));

        setTivChangeSeries([
          {
            name: metricsLabels['tiv'],
            data: groupedMetrics.tiv,
          },
        ]);
        setTivChangeYoYChange(calculateYoYChange(groupedMetrics.tiv));

        setClaimsSeries([
          {
            name: metricsLabels['claims_total'],
            data: groupedMetrics.claims_total,
          },
        ]);

        setGwpNwpValues([
          {
            label: metricsLabels['gwp'],
            value: groupedMetrics.gwp.reduce(
              (accumulator, currentValue) => accumulator + currentValue,
              0,
            ),
            format: 'dollar',
          },
          {
            label: metricsLabels['nwp'],
            value: groupedMetrics.nwp.reduce(
              (accumulator, currentValue) => accumulator + currentValue,
              0,
            ),
            format: 'dollar',
          },
        ]);

        setDamageInterruptionValues([
          {
            label: metricsLabels['property_damage'],
            value: groupedMetrics.property_damage.reduce(
              (accumulator, currentValue) => accumulator + currentValue,
              0,
            ),
            format: 'dollar',
          },
          {
            label: metricsLabels['business_interruption'],
            value: groupedMetrics.business_interruption.reduce(
              (accumulator, currentValue) => accumulator + currentValue,
              0,
            ),
            format: 'dollar',
          },
        ]);

        setAopDeductibleValues([
          {
            label: metricsLabels['aop_deductible'],
            value: groupedMetrics.aop_deductible.reduce(
              (accumulator, currentValue) => accumulator + currentValue,
              0,
            ),
            format: 'dollar',
          },
          {
            label: metricsLabels['bi_deductible'],
            value: groupedMetrics.bi_deductible.reduce(
              (accumulator, currentValue) => accumulator + currentValue,
              0,
            ),
          },
        ]);
      })
      .catch((error) => {
        console.error('There was a problem with the fetch operation:', error);
      });
  }, []);

  return (
    <div>
      <div id="overall_numbers" className="relative w-full my-4 border-b pb-4">
        <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
          KPI Summary
        </h2>
        <div className="bg-white mb-4">
          {gwpNwpValue ? <InlineCard kpis={gwpNwpValue} /> : null}
          {damageInterruptionValues ? (
            <InlineCard kpis={damageInterruptionValues} />
          ) : null}
          {aopDeductibleValues ? (
            <InlineCard kpis={aopDeductibleValues} />
          ) : null}
        </div>
      </div>
      <GrossWrittenPremium
        gwpSeries={gwpSeries}
        gwpYoYChange={gwpYoYChange}
        yearsRange={yearsRange}
        gwpChartOptions={gwpChartOptions}
      />
      <RateChange
        rateChangeSeries={rateChangeSeries}
        rateChangeYoYChange={rateChangeYoYChange}
        yearsRange={yearsRange}
        gwpChartOptions={gwpChartOptions}
      />
      <TotalInsuredValue
        tivChangeSeries={tivChangeSeries}
        tivChangeYoYChange={tivChangeYoYChange}
        yearsRange={yearsRange}
        gwpChartOptions={gwpChartOptions}
      />
      <GrossClaims
        claimsSeries={claimsSeries}
        tivChangeYoYChange={tivChangeYoYChange}
        yearsRange={yearsRange}
        gwpChartOptions={gwpChartOptions}
      />
    </div>
    // {viewDetailsTable && tableData ? (
    //   <div id="table_wrapper" className="bg-white">
    //     <Table columns={tableHeaders} data={tableData} />
    //   </div>
    // ) : null}
  );
};

export default FiveYearView;
