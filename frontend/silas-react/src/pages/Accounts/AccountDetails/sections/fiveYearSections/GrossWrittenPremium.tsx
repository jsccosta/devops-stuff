import React from 'react';

import { Tab, Tabs } from '../../../../../components/Tabs';

import { chartOptions } from '../../../../Dashboard/chart-configs';
import BarChartComponent from '../../../../../components/Charts/BarChartComponent';
import LineChart from '../../../../../components/Charts/LineChart';

import { formatToDollar, naivePercent } from '../../../../../utils/formatters';
import { metricsLabels } from '../../../../../metricsDescriptions';

const GrossWrittenPremium: React.FC = ({
  gwpSeries,
  gwpYoYChange,
  yearsRange,
  gwpChartOptions,
}) => {

  const barChartOptions = {
    plotOptions: {
      bar: {
        dataLabels: {
          position: 'top',
        },
      },
    },
    dataLabels: {
      enabled: true,
      formatter: function (val) {
        return formatToDollar(val);
      },
      offsetY: -20,
      style: {
        fontSize: '12px',
        colors: ['#304758'],
      },
    },
    xaxis: {
      categories: yearsRange,
    },
    yaxis: {
      labels: {
        formatter: (val) => {
          return formatToDollar(val / 1000000) + ' M';
        },
      },
    },
    tooltip: {
      enabled: true,
      y: {
        formatter: (value) => formatToDollar(value),
      },
    },
  };

  return (
    <div className="w-full mb-4 border-b pb-4">
      <div>
        <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
          Gross Written Premium
        </h2>
        <Tabs>
          <Tab label={`${metricsLabels['gwp']} over last 5 Years`}>
            <div className="bg-white">
              {gwpSeries ? (
                <BarChartComponent
                  options={{ ...chartOptions, ...gwpChartOptions, ...barChartOptions }}
                  label={''}
                  series={gwpSeries}
                />
              ) : (
                <div>Loading</div>
              )}
            </div>
          </Tab>
          <Tab label="Gross Written Premium Year on Year % Change">
            <div className="bg-white">
              {gwpYoYChange ? (
                <LineChart
                  label=""
                  lineChartData={[
                    {
                      name: 'Gross Written Premium Year on Year % Change',
                      data: gwpYoYChange,
                    },
                  ]}
                  customProps={{
                    dataLabels: {
                      enabled: true,
                      formatter: function (val) {
                        return naivePercent(val);
                      },
                      // offsetY: -20,
                      // style: {
                      //   fontSize: '12px',
                      //   colors: ['#304758'],
                      // },
                    },
                    xaxis: {
                      categories: yearsRange,
                    },
                    yaxis: {
                      labels: {
                        formatter: (val) => {
                          return naivePercent(val);
                        },
                      },
                    },
                  }}
                />
              ) : (
                <div>Loading</div>
              )}
            </div>
          </Tab>
        </Tabs>
      </div>
    </div>
  );
};

export default GrossWrittenPremium;
