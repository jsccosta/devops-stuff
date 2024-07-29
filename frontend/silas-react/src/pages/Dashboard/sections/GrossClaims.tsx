import React, { useState, useEffect } from 'react';
import axios from 'axios';

import PieChart from '../../../components/Charts/PieChart';
import LineChart from '../../../components/Charts/LineChart';

import { Tabs, Tab } from '../../../components/Tabs';
import InlineCard from '../../../components/InlineCard';

export const grossClaimsCardLabels = {
  gross_claims_total: 'Gross Claims Total',
  number_of_claims: 'Number of Claims',
  total_cat_perc_gwp:'As % of GWP',
  total_cat_perc_nwp:'As % of NWP',
  total_cat: 'Total (CAT)',
  total_non_cat: 'Total (Non-CAT)'
};

const lineChartCustomProps = {
  xaxis: {
    categories: ['2019', '2020', '2021', '2022', '2023'],
  },
};

const claimsChartData = [
  {
    title: 'Claims Property Damage / Business Interruption',
    data: [94, 16],
    labels: ['Business Interruption', 'Property Damage'],
  },
  {
    title: 'Claims by Region',
    data: [73, 26, 37, 93],
    labels: ['Africa', 'Latin America', 'Europe', 'USA'],
  },
  {
    title: 'Claims by Loss Type',
    data: [74, 26],
    labels: ['Non-CAT', 'CAT'],
  },
];

const grossClaimsData = [
  {
    name: 'Gross Claims Total',
    data: [10000, 5615, 5296, 3985, 2287],
  },
];

const GrossClaims: React.FC = () => {
  const [gctMetrics, setGCTMetrics] = useState(null);
  const [gctDetailsPerc, setGCTDetailsPerc] = useState(null);
  const [gctDetailsTotals, setGCTDetailsTotals] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [dep_overview] = await Promise.all([
          axios.get('/api/v1/department_overview/'),
        ]);

        setGCTMetrics([
          {
            label: grossClaimsCardLabels['gross_claims_total'],
            value: dep_overview.data.department_overview[0].gross_claims_total,
            format: 'dollar',
          },
          {
            label: grossClaimsCardLabels['number_of_claims'],
            value: dep_overview.data.department_overview[0].number_of_claims,
          },
        ]);

        setGCTDetailsPerc([
          {
            label: grossClaimsCardLabels['total_cat_perc_gwp'],
            value: dep_overview.data.department_overview[0].total_cat_perc_gwp,
            format: 'perc',
          },
          {
            label: grossClaimsCardLabels['total_cat_perc_nwp'],
            value: dep_overview.data.department_overview[0].total_cat_perc_nwp,
            format: 'perc',
          },
        ]);

        setGCTDetailsTotals([
          {
            label: grossClaimsCardLabels['total_cat'],
            value: dep_overview.data.department_overview[0].total_cat,
            format: 'dollar',
          },
          {
            label: grossClaimsCardLabels['total_non_cat'],
            value: dep_overview.data.department_overview[0].total_non_cat,
            format: 'dollar',
          },
        ]);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div id="claims" className="relative w-full my-4 border-b pb-4">
      <div className="w-full mb-4">
        <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
          Gross Claims
        </h2>

        <div className="py-4"></div>
        <div className="bg-white mb-4">
          {gctMetrics ? <InlineCard kpis={gctMetrics} /> : null}
          {gctDetailsPerc ? <InlineCard kpis={gctDetailsPerc} /> : null}
          {gctDetailsTotals ? <InlineCard kpis={gctDetailsTotals} /> : null}
        </div>

        <Tabs>
          <Tab label="Claims Breakdown">
            <div className="grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-4 xl:grid-cols-3 2xl:gap-7.5 mb-4">
              {claimsChartData.map((claimsData, index) => {
                return (
                  <PieChart
                    key={index}
                    title={claimsData.title}
                    data={claimsData.data}
                    labels={claimsData.labels}
                  />
                );
              })}
            </div>
          </Tab>
          <Tab label="Gross Claims Total - 5 Year Period">
            <div className="py-4">
              <LineChart
                lineChartData={grossClaimsData}
                customProps={lineChartCustomProps}
              />
            </div>
          </Tab>
        </Tabs>
      </div>
    </div>
  );
};

export default GrossClaims;
