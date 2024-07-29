import React from 'react';

import { Tab, Tabs } from '../../../../../components/Tabs';

import { chartOptions } from '../../../../Dashboard/chart-configs';
import BarChartComponent from '../../../../../components/Charts/BarChartComponent';
import LineChart from '../../../../../components/Charts/LineChart';

import { naivePercent, formatToDollar } from '../../../../../utils/formatters';

import { metricsLabels } from '../../../../../metricsDescriptions';

function formatNumber(num) {
  if (Math.abs(num) >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M';
  } else if (Math.abs(num) >= 1000) {
    return (num / 1000).toFixed(1) + 'K';
  } else {
    return num.toString();
  }
}

const TotalInsuredValue: React.FC = ({
  tivChangeSeries,
  tivChangeYoYChange,
  yearsRange,
  gwpChartOptions,
}) => {
  return (
    <div className="w-full mb-4 border-b pb-4">
      <div>
        <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
          Total Insured Value
        </h2>
        <Tabs>
          <Tab label={`${metricsLabels['tiv']} over last 5 Years`}>
            <div className="bg-white">
              {tivChangeSeries ? (
                <BarChartComponent
                  options={{
                    ...chartOptions,
                    ...gwpChartOptions,
                    ...{
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
                          return formatToDollar(val/1000000)+' M';
                        },
                        offsetY: -20,
                        style: {
                          fontSize: '12px',
                          colors: ['#304758'],
                        },
                      },
                      yaxis: {
                        title: {
                          text: '$ Dollars',
                        },
                        labels: {
                          formatter: (val) => {
                            return formatToDollar(val/1000000)+' M';
                          },
                        },
                      },
                      tooltip: {
                        enabled: true,
                        y: {
                          formatter: (value) => formatToDollar(value/1000000)+' M'
                        },
                      },
                    },
                  }}
                  label={''}
                  
                  series={tivChangeSeries}
                />
              ) : (
                <div>Loading</div>
              )}
            </div>
          </Tab>
          <Tab label="Total Insured Value Year on Year % Change">
            <div className="bg-white">
              {tivChangeYoYChange ? (
                <LineChart
                  label=""
                  lineChartData={[
                    {
                      name: 'Rate Change Year on Year % Change',
                      data: tivChangeYoYChange,
                    },
                  ]}
                  customProps={{
                    xaxis: {
                      categories: yearsRange,
                    },
                    dataLabels: {
                      enabled: true,
                      formatter: function (value) {
                        return Math.floor(value) + '%';
                      },
                    },
                    yaxis: {
                      title: {
                        text: 'Percentage',
                      },
                      labels: {
                        formatter: function (value) {
                          return naivePercent(value);
                        },
                      },
                    },
                    tooltip: {
                      y: {
                        formatter: function (val) {
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

export default TotalInsuredValue;
