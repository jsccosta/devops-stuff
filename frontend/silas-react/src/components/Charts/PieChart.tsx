import React, { useState } from 'react';
import { ApexOptions } from 'apexcharts';
import ReactApexChart from 'react-apexcharts';

interface ChartThreeState {
  series: number[];
}

const options: ApexOptions = {
  chart: {
    fontFamily: 'Satoshi, sans-serif',
    type: 'donut',
  },
  colors: ['#adb9f6', '#6e4ab6', '#975bce', '#7a69e9'],
  legend: {
    show: true,
    position: 'bottom',
  },

  dataLabels: {
    enabled: false,
    formatter: function (val, opts) {
      return opts.w.globals.labels[opts.seriesIndex] + ": " + val+'%'
    },
    style:{
      colors: ['#000'],
    }
  },
  responsive: [
    {
      breakpoint: 2600,
      options: {
        chart: {
          width: 380,
        },
      },
    },
    {
      breakpoint: 640,
      options: {
        chart: {
          width: 200,
        },
      },
    },
  ],
};

interface PieChartTypes {
  title: string;
  data: number[];
  labels: string[];
}

const PieChart: React.FC<PieChartTypes> = ({ title, data, labels, customOptions }) => {
  const [state, setState] = useState<ChartThreeState>({
    series: data,
  });



  const handleReset = () => {
    setState((prevState) => ({
      ...prevState,
      series: data,
    }));
  };
  handleReset;

  const chartOptions = {
    ...options, 
    labels:labels,
    ...customOptions
  }

  return (
    <div className="rounded-sm border border-stroke bg-white p-7.5 shadow-default dark:border-strokedark dark:bg-boxdark">
      <div className="mb-4 justify-between gap-4 sm:flex">
        <div>
          <h4 className="text-md font-bold text-black dark:text-white min-h-16">
            {title}
          </h4>
        </div>
      </div>
      <div className="mb-2">
        <div id="chartThree" className="mx-auto flex justify-center">
          <ReactApexChart options={chartOptions} series={state.series} type="pie" />
        </div>
      </div>
    </div>
  );
};

export default PieChart;
