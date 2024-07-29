import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import SubmissionForm from './SubmissionForm';
import Table from '../../components/Tables/Table';
import axios from 'axios';

import { CiRead, CiEdit } from 'react-icons/ci';
import { GoArchive } from 'react-icons/go';

import Layout from '../../layout/Layout';

const formatDate = (inputDate) => {
  const date = new Date(inputDate);
  const year = date.getFullYear();
  const month = ('0' + (date.getMonth() + 1)).slice(-2);
  const day = ('0' + date.getDate()).slice(-2);
  return `${year}/${month}/${day}`;
};

const columns = [
  { Header: 'Submission ID', accessor: 'id' },
  { Header: 'Underwriter', accessor: 'underwriter' },
  { Header: 'Broker', accessor: 'broker' },
  {
    Header: 'Domicile',
    accessor: 'domicile',
    Cell: ({ value }) => value.toUpperCase(),
  },
  {
    Header: 'Date Started',
    accessor: 'created_at',
    Cell: ({ value }) => formatDate(value),
  },
  {
    Header: 'Attached Files',
    accessor: 'filenames',
    Cell: ({ value }) => {
      return (
        <div className="flex flex-col">
          {value.filenames.map((filename, index) => {
            return (
              <a
                key={index}
                className="text-silas-dark hover:underline"
                href="#"
                target="_blank"
              >
                {filename}
              </a>
            );
          })}
        </div>
      );
    },
  },
];

const tableActions = [
  {
    label: 'View',
    onClick: (rowData) => console.log('View', rowData),
    icon: <CiRead />,
    classes: '',
    tooltip: 'View Documents',
  },
  {
    label: 'Edit',
    onClick: (rowData) => console.log('Edit', rowData),
    icon: <CiEdit />,
    classes: '',
    tooltip: 'Edit Submission',
  },
  {
    label: 'Archive',
    onClick: (rowData) => console.log('Delete', rowData),
    icon: <GoArchive />,
    classes: '',
    tooltip: 'Archive Submission',
  },
];

// Submission
// Underwriting
// Offer/Negotiation
// Decline
// Not Taken Up
// Bound

const Submissions: React.FC = () => {
  const [showSubmissionForm, setShowSubmissionForm] = useState(false);
  const [tableData, setTableData] = useState([]);

  const navigate = useNavigate();

  useEffect(() => {
    if (showSubmissionForm === false) {
      axios
        .get('/api/v1/submissions/')
        .then((response) => {
          console.log('Response data:', response.data);
          setTableData(response.data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  }, [showSubmissionForm]);

  return (
    <Layout>
      <div className="flex justify-between mb-4">
        {showSubmissionForm ? null : (
          <button
            id="new-submission"
            className="bg-silas-dark text-white py-2 px-4 rounded-md hover:bg-silas-medium transition duration-300 flex items-center"
            onClick={() => setShowSubmissionForm(true)}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="w-6 h-6 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M12 6v6m0 0v6m0-6h6m-6 0H6"
              ></path>
            </svg>
            New Submission
          </button>
        )}
      </div>
      {showSubmissionForm ? (
        <SubmissionForm
          closeFormClickHandler={() => setShowSubmissionForm(false)}
        />
      ) : (
        <Table
          columns={columns}
          data={tableData}
          rowClickHandler={(row) => {
            console.log({ row });
            const submissionId = row.values.id;
            navigate(`/submission/${submissionId}`);
          }}
          actions={tableActions}
          actionWrapperClass={'flex justify-between'}
        />
      )}
    </Layout>
  );
};

export default Submissions;
