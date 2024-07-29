import React, { useEffect, useState } from 'react';
import Layout from '../../../layout/Layout';
import { useParams } from 'react-router-dom';
import Breadcrumb from '../../../components/Breadcrumbs/Breadcrumb';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import './customDropdown.css';

import OneYearView from './sections/OneYearView';
import FiveYearView from './sections/FiveYearView';

import Table from '../../../components/Tables/Table';

const AccountDetails: React.FC = () => {
  const [data, setData] = useState(null);
  const [latestData, setLatestData] = useState(null);
  const [namedInsured, setNamedInsured] = useState(null);
  const [tableHeaders, setTableHeaders] = useState(null);
  const [tableData, setTableData] = useState(null);

  const [viewDetailsTable, setViewDetailsTable] = useState(false);

  const { accountId } = useParams();

  const options = [
    { value: 1, label: 'One Year View' },
    { value: 5, label: 'Five Year View' },
  ];

  const [selectedRange, setSelectedRange] = useState(options[0]);

  useEffect(() => {
    const apiUrl = `/api/v1/new_metrics?company_id=${accountId}`;

    // Make the API call using the Fetch API
    fetch(apiUrl)
      .then((response) => {
        // Check if the response is successful
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // Parse the response as JSON
        return response.json();
      })
      .then((data) => {
        const companyMetrics = data.company_metrics[0];
        setNamedInsured(companyMetrics.named_insured);
        setData(data);
      })
      .catch((error) => {
        console.error('There was a problem with the fetch operation:', error);
      });
  }, [selectedRange]);

  return (
    <Layout>
      <Breadcrumb pageName="Account Details" />
      {namedInsured ? (
        <h2 className="text-4xl font-bold">{namedInsured}</h2>
      ) : null}
      <div className="flex justify-between items-center mb-4">
        <Dropdown
          options={options}
          onChange={(selection) => {
            setSelectedRange(selection);
          }}
          value={selectedRange}
          placeholder="Select an option"
        />

        <button
          id="toggle-table"
          className="min-w-36 bg-silas-dark text-white py-2 px-4 rounded-md hover:bg-silas-medium transition duration-300 flex items-center"
          onClick={() => setViewDetailsTable(!viewDetailsTable)}
        >
          {`${viewDetailsTable ? 'Hide' : 'Show'} Detailed Table`}
        </button>
      </div>

      {selectedRange.value === 1 ? (
        <OneYearView viewDetailsTable={viewDetailsTable} />
      ) : (
        <FiveYearView viewDetailsTable={viewDetailsTable} />
      )}

      {viewDetailsTable && tableData ? (
        <div id="table_wrapper" className="bg-white">
          <Table columns={tableHeaders} data={tableData} />
        </div>
      ) : null}
    </Layout>
  );
};

export default AccountDetails;
