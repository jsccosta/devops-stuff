export function extractFields(dataset, fieldsToExtract) {
    return dataset.map((item) => {
      const extractedItem = {};
      fieldsToExtract.forEach((field) => {
        extractedItem[field] = item[field];
      });
      return extractedItem;
    });
  }
  
  export function convertToChartData(data, metricNames, seriesNames) {
    const series = [];
  
    metricNames.forEach((metric, index) => {
      const metricData = [];
      data.forEach((item) => {
        metricData.push(item[metric]);
      });
  
      series.push({
        name: seriesNames[index],
        data: metricData,
      });
    });
  
    return series;
  }