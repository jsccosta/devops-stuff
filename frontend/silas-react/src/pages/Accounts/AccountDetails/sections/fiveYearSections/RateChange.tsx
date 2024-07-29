import React from 'react';

import { Tab, Tabs } from '../../../../../components/Tabs';

import { naivePercent } from '../../../../../utils/formatters';

import { chartOptions } from '../../../../Dashboard/chart-configs';
import BarChartComponent from '../../../../../components/Charts/BarChartComponent';
import LineChart from '../../../../../components/Charts/LineChart';

import { metricsLabels } from '../../../../../metricsDescriptions';

const RateChange: React.FC = ({rateChangeSeries, rateChangeYoYChange, yearsRange,  gwpChartOptions}) => {

  return (
      <div className="w-full mb-4 border-b pb-4">
        <div>
          <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
            Rate Change
          </h2>
          <Tabs>
            <Tab label={`${metricsLabels['rate_change']} over last 5 Years`}>
              <div className="bg-white">
                {rateChangeSeries ? (
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
                            // return formatToDollar(val);
                            return naivePercent(val)
                          },
                          offsetY: -20,
                          style: {
                            fontSize: '12px',
                            colors: ['#304758'],
                          },
                        },
                        yaxis: {
                          title: {
                            text: 'Percentage',
                          },
                          labels: {
                            formatter: (val) => {
                              return naivePercent(val);
                            },
                          },
                        },
                        tooltip: {
                          enabled: true,
                          y: {
                            formatter: (value) => naivePercent(value),
                          },
                        },
                      },
                    }}
                    label={''}
                    series={rateChangeSeries}
                  />
                ) : (
                  <div>Loading</div>
                )}
              </div>
            </Tab>
            <Tab label="Rate Change Year on Year % Change">
              <div className="bg-white">
                {rateChangeYoYChange ? (
                  <LineChart
                    label=""
                    lineChartData={[
                      {
                        name: 'Rate Change Year on Year % Change',
                        data: rateChangeYoYChange,
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
                            return Math.floor(val) + '%';
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

export default RateChange;
