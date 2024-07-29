export function convertRotatedData(rotatedData) {
  const accountDetailsData = [];

  // Iterate over the rotatedData object
  // debugger;
  for (const [namedInsured, data] of Object.entries(rotatedData)) {
    const rowData = { named_insured: namedInsured };

    // Iterate over the keys (properties) of each named insured's data
    // let isFirstEntry = true;
    for (const [key, value] of Object.entries(data)) {
      // debugger;
      if (key === 'company_id' || key === 'id') {
        // isFirstEntry = false;
        continue;
      }
      let dataRow;
      // const accessor = `year_minus_${Object.keys(data).indexOf(key)}`;
      // rowData[accessor] = value;

      const valuesToObject = Object.values(value);

      dataRow = {
        item: convertSnakeCaseToHumanReadable(key),
        year_minus_1: valuesToObject[4],
        year_minus_2: valuesToObject[3],
        year_minus_3: valuesToObject[2],
        year_minus_4: valuesToObject[1],
        year_minus_5: valuesToObject[0],
      };
      accountDetailsData.push(dataRow);
    }
  }

  return accountDetailsData;
}

export function convertSnakeCaseToHumanReadable(str) {
  // Split the string by underscores
  const words = str.split('_');

  // Capitalize the first letter of each word
  const capitalizedWords = words.map(
    (word) => word.charAt(0).toUpperCase() + word.slice(1),
  );

  // Join the words with space
  const humanReadableStr = capitalizedWords.join(' ');

  return humanReadableStr;
}

export function convertTableHeaders(tableHeaders) {
  const accountDetailsColumns = [];

  // Add named_insured as the first column
  accountDetailsColumns.push({ Header: tableHeaders[0], accessor: 'item' });

  // Add years as subsequent columns
  for (let i = 1; i < tableHeaders.length; i++) {
    accountDetailsColumns.push({
      Header: tableHeaders[i],
      accessor: `year_minus_${i}`,
    });
  }

  return accountDetailsColumns;
}

export function rotateData(inputData) {
  let rotatedData = {};
  let tableHeaders = [];

  inputData.data.forEach((item) => {
    const namedInsured = item.named_insured;
    const year = item.year;

    // Add named_insured to table headers if it's not already present
    if (!tableHeaders.includes(namedInsured)) {
      tableHeaders.push(namedInsured);
    }

    if (!rotatedData[namedInsured]) {
      rotatedData[namedInsured] = {};
    }
    for (const [key, value] of Object.entries(item)) {
      if (key !== 'named_insured' && key !== 'year') {
        if (!rotatedData[namedInsured][key]) {
          rotatedData[namedInsured][key] = {};
        }
        rotatedData[namedInsured][key][year] = value;
      }
    }
  });

  // Add years to table headers if they're not already present
  inputData.data.forEach((item) => {
    const year = item.year;
    if (!tableHeaders.includes(year)) {
      tableHeaders.push(year);
    }
  });

  // Sort table headers in ascending order
  // tableHeaders.sort();
  tableHeaders.sort((a, b) => b - a);

  return {
    rotatedData: rotatedData,
    tableHeaders: tableHeaders,
  };
}
