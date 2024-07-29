import React from 'react';

import { Tabs, Tab } from '../../../components/Tabs';
import LineChart from '../../../components/Charts/LineChart';


const lineChartCustomProps = {
  xaxis: {
    categories: ['2019', '2020', '2021', '2022', '2023'],
  },
};

const totalInsuredValue = [
  {
    name: 'Total Insured Value % Change (Year on Year)',
    data: [13, 65, 59, 98, 28],
  },
];

const tiv_gwpYoy = [
  {
    name: 'Total Insured Value %',
    data: [89, 65, 59, 98, 28],
  },
  {
    name: 'Gross Written Premium %',
    data: [38, 75, 39, 88, 58],
  },
];

const tiv5Years = [
  {
    name: 'Total Insured Value in 5 years',
    data: [10000,65000, 45000, 98000, 22000],
  },
]

const TotalInsuredValue: React.FC = () => {
  return (
    <div id="occupancy-split" className="relative w-full my-4 border-b pb-4">
      <div className="w-full mb-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-title-md2 font-semibold text-black dark:text-white">
            Total Insured Value
          </h2>
        </div>
        <div className="py-4">
          <Tabs>
            <Tab label="TIV (Year on Year)">
              <div className="py-4">
                <LineChart
                  lineChartData={totalInsuredValue}
                  customProps={lineChartCustomProps}
                />
              </div>
            </Tab>
            <Tab label="TIV x GWP YoY">
              <div className="py-4">
                <LineChart
                  lineChartData={tiv_gwpYoy}
                  customProps={lineChartCustomProps}
                />
              </div>
            </Tab>
            <Tab label="Total Insured Value 5 Years">
              <div className="py-4">
                <LineChart
                  lineChartData={tiv5Years}
                  customProps={lineChartCustomProps}
                />
              </div>
            </Tab>
          </Tabs>
        </div>
      </div>
    </div>
  );
};

export default TotalInsuredValue;
