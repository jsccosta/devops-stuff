export const lineChartBaseProps = {
    chart: {
      height: 350,
      type: 'line',
      zoom: {
        enabled: false,
      },
    },
    colors: ['#6e4ab6', '#adb9f6', '#975bce', '#7a69e9'],
    dataLabels: {
      enabled: true,
    },
    stroke: {
      curve: 'straight',
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5,
      },
    }
};

export const barChartComponentProps = {
    chart: {
      type: 'bar',
      height: 350,
    },
    colors: ['#adb9f6', '#6e4ab6', '#975bce', '#7a69e9'],
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