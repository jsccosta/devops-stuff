export const sideBySideBarChartProps = {
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
    yaxis: {
      title: {
        text: 'Amount',
      },
      labels: {
        formatter: function (value) {
          return value / 1000 + 'K'; // Divide the value by 1000
        },
      },
    },
    tooltip: {
      shared: true,
      intersect: false,
      y: {
        formatter: function (val) {
          return '$ ' + val / 1000 + 'K';
        },
      },
    },
  };

  
  export const accountsWrittenPremiumMonth = {
    label: 'Accounts Written Premium by Month between the years 2022 and 2023',
    series: [
      {
        name: '2023',
        data: [1250000, 1200000, 1150000, 1100000, 1050000, 1000000, 950000, 900000, 850000, 800000, 750000, 700178]

      },
      {
        name: '2022',
        data: [1090891, 1189123, 1287355, 1385587, 1483819, 1582051, 1680283, 1778515, 1876747, 1974979, 2073211, 2114651]

      },
    ],
  };







  export const accountsOccupancyGeneral = {
    label: 'Accounts Occupancy (General)',
    series: [
      {
        name: 'Occupancy',
        data: [123, 4, 93, 24, 66],
      },
    ],
  };
  
  export const accountsWrittenMonth = {
    label: 'Accounts Written by Month',
    series: [
      {
        name: 'Accounts Written',
        data: [123, 4, 93, 24, 66, 12, 84, 33, 9, 16, 77, 33],
      },
    ],
  };

  export const gwpVarianceData = [
    {
      name: 'GWP % Change',
      data: [30, 14, 85, 39, 77],
    },
  ];