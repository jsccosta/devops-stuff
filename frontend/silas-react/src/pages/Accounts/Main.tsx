import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Layout from '../../layout/Layout';
import Table from '../../components/Tables/Table';

import { formatToDollar, naivePercent } from '../../utils/formatters';

const columns = [
  {
    Header: 'Company ID', // This header will not be displayed
    accessor: 'company_id',
  },
  { Header: 'Named Insured', accessor: 'named_insured' },
  { Header: 'Underwriter', accessor: 'underwriter' },
  { Header: 'Broker', accessor: 'broker' },
  { Header: 'Inception Date', accessor: 'inception_date' },
  {
    Header: 'TIV',
    accessor: 'tiv',
    Cell: ({ value }) => `${formatToDollar(value)}`,
  },
  {
    Header: 'Occupancy',
    accessor: 'occupancy',
  },
  {
    Header: 'Gross Written Premium',
    accessor: 'gwp',
    Cell: ({ value }) => `${formatToDollar(value)}`,
  },
  {
    Header: 'Base Rate % ',
    accessor: 'base_rate',
    Cell: ({ value }) => `${naivePercent(value)}`,
  },
  {
    Header: 'Loss Ratio %',
    accessor: 'loss_ratio',
    Cell: ({ value }) => `${naivePercent(value)}`,
  },
];

const extraProps = { hiddenColumns: ['company_id'] };

const Accounts: React.FC = () => {
  // Define state to store the fetched data
  const [data, setData] = useState(null);

  const navigate = useNavigate();

  // Define useEffect hook to make the API call when the component mounts
  useEffect(() => {
    // Define the URL of the API endpoint
    const apiUrl = '/api/v1/accounts/';

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
        // Update the component state with the fetched data
        setData(data);
      })
      .catch((error) => {
        console.error('There was a problem with the fetch operation:', error);
      });
  }, []);

  return (
    <Layout>
      <div id="accounts" className="relative w-full my-4 pb-4">
        <div className="w-full mb-4">
          <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
            Accounts
          </h2>

          {data ? (
            <div id="table_wrapper" className="bg-white">
              <Table
                columns={columns}
                data={data.companies}
                extraProps={extraProps}
                enableRowClick={true}
                rowClickHandler={
                  (row) => {
                    const companyId = row.values.company_id;
                    navigate(`/accounts/${companyId}`);
                  }
                }
              />
            </div>
          ) : (
            <>Loading...</>
          )}
        </div>
      </div>
      <div className="w-56"></div>
    </Layout>
  );
};

export default Accounts;
