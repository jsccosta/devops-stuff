import React, { useState } from 'react';
import ReactApexChart from 'react-apexcharts';

import { barChartComponentProps } from './base_props';

interface ChartTwoState {
  series: {
    name: string;
    data: number[];
  }[];
}

interface BarChartProps {
  label: string;
  series: [
    {
      name: string;
      data: number[];
    },
  ];
}

const BarChartComponent: React.FC<BarChartProps> = ({
  label,
  series,
  options,
}) => {
  const chartOptions = {
    ...barChartComponentProps,
    ...options,
  };

  const [state, setState] = useState<ChartTwoState>({
    series: series,
  });

  const handleReset = () => {
    setState((prevState) => ({
      ...prevState,
    }));
  };
  handleReset;

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
            options={chartOptions}
            series={state.series}
            type="bar"
            height={350}
          />
        </div>
      </div>
    </div>
  );
};

export default BarChartComponent;
