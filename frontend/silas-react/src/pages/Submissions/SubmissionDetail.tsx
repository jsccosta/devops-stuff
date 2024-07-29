import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import Table from '../../components/Tables/Table';
import axios from 'axios';

import { CiRead, CiEdit } from 'react-icons/ci';
import { GoArchive } from 'react-icons/go';

import { Tooltip } from 'react-tooltip';

import Layout from '../../layout/Layout';

// Submission
// Underwriting
// Offer/Negotiation
// Decline
// Not Taken Up
// Bound

function formatDate(inputDate) {
  const date = new Date(inputDate);

  const formattedDate = new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).format(date);

  return formattedDate;
}

const EditableText = ({ text }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editedText, setEditedText] = useState(text);

  const handleDoubleClick = () => {
    setIsEditing(true);
  };

  const handleBlur = () => {
    setIsEditing(false);
  };

  const handleChange = (e) => {
    setEditedText(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      setIsEditing(false);
    }
  };

  const handleToggleEditMode = () => {
    setIsEditing(!isEditing);
  };

  return (
    <div>
      {isEditing ? (
        <input
          className="w-96"
          type="text"
          value={editedText}
          onChange={handleChange}
          onBlur={handleBlur}
          onKeyDown={handleKeyDown}
          autoFocus
        />
      ) : (
        <div className="flex w-full">
          <div className="w-96" onDoubleClick={handleDoubleClick}>
            {editedText}
          </div>
          <button className="ml-4" onClick={handleToggleEditMode}>
            Edit
          </button>
        </div>
      )}
    </div>
  );
};

const FileActions = ({ label, icon, tooltip }) => {
  return (
    <button
      id={label}
      key={label}
      // onClick={() => onClick()}
    >
      {icon}

      <Tooltip id="table-tooltip" anchorSelect={`#${label}`} place="top">
        {tooltip}
      </Tooltip>
    </button>
  );
};

const SubmissionDetail: React.FC = () => {
  const { submissionId } = useParams();

  const [submissionInfo, setSubmissionInfo] = useState(null);

  useEffect(() => {
    const apiUrl = `/api/v1/submission?submission_id=${submissionId}`;
    axios
      .get(apiUrl)
      .then((response) => {
        console.log('Response data:', response.data[0]);
        setSubmissionInfo(response.data[0]);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <Layout>
      {submissionInfo ? (
        <div className="rounded-sm mb-4 border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
          <div className="border-b border-stroke py-4 px-6.5 dark:border-strokedark">
            <div className="flex items-center justify-between">
              <h3 className="flex w-48 text-right  font-medium text-black dark:text-white">
                <div className=''></div>
                Submission Number: {submissionInfo.id}
              </h3>
              <div className="font-medium text-black dark:text-white">
                Submitted on: {formatDate(submissionInfo.created_at)}
              </div>
            </div>
          </div>

          <div className="flex flex-col gap-5.5 p-6.5 pb-1">
            <div id="submission-info" className="flex mb-3">
              <div className="w-40 text-right  font-medium block text-black dark:text-white">
                Account Name:
              </div>
              <div className="block ml-4 text-black dark:text-white">
                <EditableText text={submissionInfo.account_name} />
              </div>
            </div>
            <div id="submission-info" className="flex mb-3">
              <div className="w-40 text-right  font-medium block text-black dark:text-white">
                Underwriter:
              </div>
              <div className="block ml-4 text-black dark:text-white">
                <EditableText text={submissionInfo.underwriter} />
              </div>
            </div>
            <div id="submission-info" className="flex mb-3">
              <div className="w-40 text-right  font-medium block text-black dark:text-white">
                Broker:
              </div>
              <div className="block ml-4 text-black dark:text-white">
                <EditableText text={submissionInfo.broker} />
              </div>
            </div>
            <div id="submission-info" className="flex mb-3">
              <div className="w-40 text-right  font-medium block text-black dark:text-white">
                Statement Of Value:
              </div>
              <div className="block ml-4 text-black dark:text-white">
                <div className="flex w-full">
                  <div className="w-96">
                    {submissionInfo.filenames.filenames[0]}
                  </div>
                  <button className="ml-4">Edit</button>
                </div>
              </div>
            </div>
            <div id="submission-info" className="flex mb-3">
              <div className="w-40 text-right  font-medium block text-black dark:text-white">
                Policy Document:
              </div>
              <div className="block ml-4 text-black dark:text-white">
                <div className="flex w-full">
                  <div className="w-96">
                    {submissionInfo.filenames.filenames[1]}
                  </div>
                  <button className="ml-4">Edit</button>
                </div>
              </div>
            </div>
            <div id="submission-info" className="flex mb-3">
              <div className="w-40 text-right  font-medium block text-black dark:text-white">
                Engineering Report:
              </div>
              <div className="block ml-4 text-black dark:text-white">
                <div className="flex w-full">
                  <div className="w-96">
                    {submissionInfo.filenames.filenames[2]}
                  </div>
                  <button className="ml-4">Edit</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      ) : (
        <div>Loading...</div>
      )}
    </Layout>
  );
};

export default SubmissionDetail;
