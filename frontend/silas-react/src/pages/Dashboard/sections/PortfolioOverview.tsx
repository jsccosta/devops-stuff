import React, { useState, useEffect } from 'react';
import axios from 'axios';

import { Tabs, Tab } from '../../../components/Tabs';
import StackedDataCard from '../../../components/StackedDataCard';
import LineChart from '../../../components/Charts/LineChart';
import BarChartComponent from '../../../components/Charts/BarChartComponent';

import { extractFields, convertToChartData } from '../helpers';
import { metricsLabels } from '../../../metricsDescriptions';

import {
  sideBySideBarChartProps,
  gwpVarianceData,
} from '../dummy-data';

const lineChartCustomProps = {
  xaxis: {
    categories: ['2019', '2020', '2021', '2022', '2023'],
  },
};

const rateChangeYoY = [
  {
    name: 'Rate Change Year on Year',
    data: [0.23, 0.45, 0.065, 0.81, 0.34],
  },
];



const PortfolioOverview: React.FC = () => {
  const [netWrittenPremiums, setNetWrittenPremiums] = useState(null);
  const [portfolioMetrics, setPortfolioMetrics] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [dep_overview, accts_yoy] = await Promise.all([
          axios.get('/api/v1/department_overview/'),
          axios.get('/api/v1/accounts_yoy/'),
        ]);

        setPortfolioMetrics([
          // gwp
          [
            {
              label: metricsLabels['gwp'],
              value: dep_overview.data.department_overview[0].gwp,
              format: 'dollar'

            },
            {
              label: metricsLabels['nwp'],
              value: dep_overview.data.department_overview[0].nwp,
              format: 'dollar'
            }
          ],
          // generalMetrics
          [
            {
              label: metricsLabels['brokerage'],
              value: dep_overview.data.department_overview[0].brokerage,
              format: 'perc'
            },
            {
              label: metricsLabels['fees_and_commisions'],
              value:
                dep_overview.data.department_overview[0].fees_and_commissions,
                format: 'perc'
            },
            {
              label: metricsLabels['loss_ratio'],
              value: dep_overview.data.department_overview[0].loss_ratio,
              format: 'perc'
            },
            
          ],
        ]);


        const writtenPremiumFields = ['date', 'gwp_by_month', 'nwp_by_month'];
        const writtenPremiums = extractFields(
          accts_yoy.data.accounts_yoy,
          writtenPremiumFields,
        );

        const metricNames = ['gwp_by_month', 'nwp_by_month'];
        const seriesNames = ['Gross Written Premium', 'Net Written Premium'];

        const newData = convertToChartData(
          writtenPremiums,
          metricNames,
          seriesNames,
        );

        setNetWrittenPremiums(newData);

        console.log({newData})

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div id="portfolio_overview" className="flex flex-col border-b my-4 pb-4">
      <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
        Portfolio Overview
      </h2>
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 md:gap-6 xl:grid-cols-2 2xl:gap-7.5 mb-4 ">
        {portfolioMetrics?.map((metric, index) => {
          return <StackedDataCard key={index} kpis={metric} />;
        })}
      </div>
      <Tabs>
        <Tab label="Written Premium by Month">
          <div className="py-4">
            {netWrittenPremiums ? (
              <BarChartComponent
                series={netWrittenPremiums}
                options={sideBySideBarChartProps}
              />
            ) : (
              <>Loading...</>
            )}
          </div>
        </Tab>
        <Tab label="GWP % Change (Year on Year)">
          <div className="py-4">
            <LineChart lineChartData={gwpVarianceData} customProps={lineChartCustomProps}/>
          </div>
        </Tab>
        <Tab label="Rate Change (Year on Year)">
          <div className="py-4">
            <LineChart lineChartData={rateChangeYoY} customProps={lineChartCustomProps}/>
          </div>
        </Tab>

      </Tabs>
    </div>
  );
};


export default PortfolioOverview;
