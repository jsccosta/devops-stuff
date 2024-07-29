import React, { useState, useEffect } from 'react';
import {
  ChangeEvent,
  Dispatch,
  SetStateAction,
  FormEvent,
  ReactNode,
} from 'react';
import { useParams } from 'react-router-dom';

import { Tab, Tabs } from '../../components/Tabs';

import Table from '../../components/Tables/Table';
import axios from 'axios';

import { CiRead, CiEdit } from 'react-icons/ci';
import { GoArchive } from 'react-icons/go';

import FileUpload from '../../components/FilesUploader/FileUpload';

import { Tooltip } from 'react-tooltip';

import Layout from '../../layout/Layout';

// Submission
// Underwriting
// Offer/Negotiation
// Decline
// Not Taken Up
// Bound
type FileState = File | null;

function capitalizeWords(str) {
  return str
    .split(' ')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function CloseButton({ onClickHandler }) {
  return (
    <div className="tooltip-anchor relative inline-block">
      <button
        className="p-2 rounded-full text-gray-600 hover:bg-gray-200 focus:outline-none"
        onClick={() => {
          onClickHandler();
        }}
      >
        <svg
          className="w-4 h-4"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <line x1="18" y1="6" x2="6" y2="18" />
          <line x1="6" y1="6" x2="18" y2="18" />
        </svg>
      </button>
      <Tooltip id="my-tooltip" anchorSelect=".tooltip-anchor" place="top">
        Close Form
      </Tooltip>
    </div>
  );
}

const EngineeringReports: React.FC = () => {
  const [file, setFile] = useState<FileState>(null);
  const [processedDocuments, setProcessedDocuments] = useState<FileState>(null);
  const [showSubmissionForm, setShowSubmissionForm] = useState(false);

  useEffect(() => {
    const apiUrl = `/api/v1/files/get_summaries/`;

    if(showSubmissionForm){
      return;
    }

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
        setProcessedDocuments(data);
      })
      .catch((error) => {
        console.error('There was a problem with the fetch operation:', error);
      });
  }, [showSubmissionForm]);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setFile(file);
    }
  };

  // Function to handle form submission
  const handleSubmit = async (
    event: FormEvent<HTMLFormElement>,
  ): Promise<void> => {
    event.preventDefault();

    // Create FormData object and append files
    const formData = new FormData();

    formData.append('file', file);

    // ToDo: Change endpoint URL
    try {
      const response = await axios.post(
        '/api/v1/files/upload_for_summarization/',
        formData,
        {
          headers: {
            accept: 'application/json',
            'Content-Type': 'multipart/form-data',
          },
        },
      );
      if (response.status === 200) {
        setShowSubmissionForm(false);
      }
      console.log('Upload successful:', response.data);
    } catch (error) {
      console.error('Upload failed:', error);
    }
  };

  // work needs to be done here to improve the look and feel of this thing

  return (
    <Layout>
      <div className="flex flex-col">
        <h2 className="mb-16 text-title-md2 font-semibold text-black dark:text-white">
          Report Summarization
        </h2>

        <div className="flex">
          {showSubmissionForm ? (
            <>
              <h3 className="font-medium text-black dark:text-white">
                Upload New Report
              </h3>
              <CloseButton onClickHandler={() => setShowSubmissionForm(false)} />
            </>
          ) : (
            <button
              id="new-submission"
              className="w-56 bg-silas-dark text-white py-2 px-4 rounded-md hover:bg-silas-medium transition duration-300 flex items-center"
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

        <div className="flex justify-between my-4">
          {!showSubmissionForm ? (
            <div className="bg-white w-full">
              <table className="table-auto w-full">
                <thead className="bg-blue-100">
                  <tr>
                    <th className="px-4 py-2 ">Report Name</th>
                    {/* <th className="px-4 py-2 ">Processed at</th> */}
                    <th className="px-4 py-2 ">Report Link</th>
                  </tr>
                </thead>
                <tbody>
                  {processedDocuments ? (
                    processedDocuments.map((document, index) => {
                      const docName = capitalizeWords(
                        document.filename
                          .split('.')[0]
                          // .split('_')
                          // .slice(1)
                          // .join(' '),
                      );


                      return (
                        <tr
                          className={` bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600`}
                        >
                          <td className={`w-4 p-4 text-center`}>{docName}</td>
                          {/* <td className={`w-4 p-4 text-center`}>
                            {document.processed_at.split(' ')[0]}
                          </td> */}
                          <td
                            className={`w-4 p-4 text-center hover:cursor-pointer`}
                          >
                            <a
                              key={index}
                              className="text-silas-dark hover:underline"
                              href={document.file_path.url}
                              target="_blank"
                            >
                              Link
                            </a>
                          </td>
                        </tr>
                      );
                    })
                  ) : (
                    <tr>
                      <td
                        className="p-8 text-center bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                        colSpan={3}
                      >
                        No data available
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="bg-white w-full">
              <form onSubmit={handleSubmit}>
                <div className="flex flex-col gap-5.5 p-6.5 pb-1">
                  <div id="eng_rep-file-upload">
                    <input
                      onChange={handleFileChange}
                      type="file"
                      multiple
                      className="w-full cursor-pointer rounded-lg border-[1.5px] border-stroke bg-transparent outline-none transition file:mr-5 file:border-collapse file:cursor-pointer file:border-0 file:border-r file:border-solid file:border-stroke file:bg-whiter file:py-3 file:px-5 file:hover:bg-primary file:hover:bg-opacity-10 focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:file:border-form-strokedark dark:file:bg-white/30 dark:file:text-white dark:focus:border-primary"
                    />
                  </div>
                </div>
                <div className="p-6.5">
                  <button
                    type="submit"
                    className="inline-flex rounded bg-silas-dark px-3 py-1 font-medium text-white hover:bg-opacity-90 sm:px-6 sm:py-2.5"
                  >
                    Load document
                  </button>
                </div>
              </form>
            </div>
          )}
        </div>
      </div>
    </Layout>
  );
};

export default EngineeringReports;
