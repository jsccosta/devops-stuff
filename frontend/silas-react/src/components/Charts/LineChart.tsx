import React from 'react';
import ReactApexChart from 'react-apexcharts';

import { lineChartBaseProps } from './base_props';

const LineChart: React.FC = ({label='', lineChartData, customProps={} }) => {

  const lineChartProps = {
    ...lineChartBaseProps,
    ...customProps
  }

  return (
    <div className="col-span-12 rounded-sm border border-stroke bg-white p-7.5 shadow-default dark:border-strokedark dark:bg-boxdark xl:col-span-4">
      <div className="mb-4 justify-between gap-4 sm:flex">
        <div>
          <h4 className="text-sm text-black dark:text-white">{label}</h4>
        </div>
      </div>
      <div>
        <div id="chartTwo" className="-ml-5 -mb-9">
          <ReactApexChart
            options={lineChartProps}
            series={lineChartData}
            type="line"
            height={350}
          />
        </div>
      </div>
    </div>
  );
};

export default LineChart;
