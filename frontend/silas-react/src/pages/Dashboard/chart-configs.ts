const baseConfig = {
  chart: {
    type: 'bar',
    height: 350,
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '80%',
      endingShape: 'rounded',
    },
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent'],
  },
  fill: {
    opacity: 1,
  },
};

const customChartOptions = {
  xaxis: {
    categories: [
      'Hotels',
      'Manufacturing',
      'Pharmaceuticals',
      'Food',
      'Retail',
    ],
  },

  yaxis: {
    title: {
      text: 'Quantity',
    },
    labels: {
      formatter: function (value) {
        return value;
      },
    },
  },
  tooltip: {
    shared: true,
    intersect: false,
    y: {
      formatter: function (val) {
        return val;
      },
    },
  },
};

const acctsWrittenMonthCustomOptions = {
  plotOptions: {
    bar: {
      dataLabels: {
        position: 'top',
      },
    },
  },
  dataLabels: {
    enabled: true,
    offsetY: -20,
    style: {
      fontSize: '12px',
      colors: ['#304758'],
    },
  },
  xaxis: {
    categories: [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ],
  },
};

export const chartOptions = {
  ...baseConfig,
  ...customChartOptions,
};

export const acctsWrittenMonthOptions = {
  ...baseConfig,
  ...acctsWrittenMonthCustomOptions,
};

export const stackedOptions = {
  chart: {
    type: 'bar',
    height: 350,
    stacked: true,
    toolbar: {
      show: true,
    },
    zoom: {
      enabled: true,
    },
  },
  responsive: [
    {
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -10,
          offsetY: 0,
        },
      },
    },
  ],
  plotOptions: {
    bar: {
      horizontal: false,
      dataLabels: {
        total: {
          enabled: true,
          style: {
            fontSize: '13px',
            fontWeight: 900,
          },
        },
      },
    },
  },
  xaxis: {
    categories: [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ],
  },
  legend: {
    position: 'right',
    offsetY: 40,
  },
  tooltip: {
    shared: true,
    intersect: false,
    y: {
      formatter: function (val) {
        return val.toFixed(0);
      },
    },
  },
  fill: {
    opacity: 1,
  },
};
