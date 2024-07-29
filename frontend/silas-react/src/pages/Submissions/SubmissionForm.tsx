import React, { ChangeEvent, useState, useRef } from 'react';
import axios from 'axios';
import { Tooltip } from 'react-tooltip';

import Selector from '../../components/Selector/Selector';

const domicileOptions = [
  { id: 'select', label: 'Select a Value' },
  { id: 'usa', label: 'USA' },
  { id: 'canada', label: 'Canada' },
  { id: 'uk', label: 'UK' },
];

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

const SubmissionForm = ({
  closeFormClickHandler
}) => {
  const [files, setFiles] = useState<File[]>([]);
  const [selectedDomicile, setSelectedDomicile] = useState(
    domicileOptions[0].label,
  );
  const [accountName, setAccountName] = useState('');
  const [underwriter, setUnderwriter] = useState('');
  const [broker, setBroker] = useState('');

  const sovRef = useRef(null);
  const policyRef = useRef(null);
  const engRef = useRef(null);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const newFiles: File[] = Array.from(event.target.files as FileList);
    setFiles([...files, ...newFiles]);
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const formDataToSend = new FormData();
    formDataToSend.append('account_name', accountName);
    formDataToSend.append('underwriter', underwriter);
    formDataToSend.append('domicile', selectedDomicile);
    formDataToSend.append('broker', broker);

    if (files) {
      for (let i = 0; i < files.length; i++) {
        formDataToSend.append('files', files[i]);
      }
    }

    await axios
      .post('/api/v1/submission/', formDataToSend)
      .then((response) => {
        console.log('Upload successful:', response.data);
        setAccountName('');
        setBroker('');
        setUnderwriter('');
        setSelectedDomicile('select');
        setFiles(null);
        sovRef.current.value = '';
        policyRef.current.value = '';
        engRef.current.value = '';
        closeFormClickHandler()
      })
      .catch((error) => {
        console.error('Upload failed:', error);
      });
  };

  return (
    <div className="rounded-sm mb-4 border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
      <div className="border-b border-stroke py-4 px-6.5 dark:border-strokedark">
        <div className='flex items-center justify-between'>
        <h3 className="font-medium text-black dark:text-white">
          New Submission
        </h3>
        <CloseButton onClickHandler={closeFormClickHandler} />
        </div>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="flex flex-col gap-5.5 p-6.5 pb-1">
          <div id="input">
            <label className="mb-3 block text-black dark:text-white">
              Account Name
            </label>
            <input
              type="text"
              placeholder="Account Name"
              value={accountName}
              onChange={(e) => setAccountName(e.target.value)}
              className="w-full rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
            />
          </div>
          <div id="input">
            <label className="mb-3 block text-black dark:text-white">
              Underwriter
            </label>
            <input
              type="text"
              placeholder="Underwriter"
              value={underwriter}
              onChange={(e) => setUnderwriter(e.target.value)}
              className="w-full rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
            />
          </div>
          <div className="flex">
            <Selector
              id={'domicile-selector'}
              label={'Domicile'}
              options={domicileOptions}
              value={selectedDomicile}
              onChange={(selectedDomicile) =>
                setSelectedDomicile(selectedDomicile)
              }
            />
            <div id="input" className="flex-grow">
              <label className="mb-3 block text-black dark:text-white">
                Broker
              </label>
              <input
                type="text"
                placeholder="Broker"
                value={broker}
                onChange={(e) => setBroker(e.target.value)}
                className="w-full rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
              />
            </div>
          </div>
          <div id="sov-file-upload">
            <label className="mb-3 block text-black dark:text-white">
              Attach SOV
            </label>
            <input
              onChange={handleFileChange}
              type="file"
              multiple
              ref={sovRef}
              className="w-full cursor-pointer rounded-lg border-[1.5px] border-stroke bg-transparent outline-none transition file:mr-5 file:border-collapse file:cursor-pointer file:border-0 file:border-r file:border-solid file:border-stroke file:bg-whiter file:py-3 file:px-5 file:hover:bg-primary file:hover:bg-opacity-10 focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:file:border-form-strokedark dark:file:bg-white/30 dark:file:text-white dark:focus:border-primary"
            />
          </div>
          <div id="policy-file-upload">
            <label className="mb-3 block text-black dark:text-white">
              Attach Policy Document
            </label>
            <input
              onChange={handleFileChange}
              type="file"
              multiple
              ref={policyRef}
              className="w-full cursor-pointer rounded-lg border-[1.5px] border-stroke bg-transparent outline-none transition file:mr-5 file:border-collapse file:cursor-pointer file:border-0 file:border-r file:border-solid file:border-stroke file:bg-whiter file:py-3 file:px-5 file:hover:bg-primary file:hover:bg-opacity-10 focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:file:border-form-strokedark dark:file:bg-white/30 dark:file:text-white dark:focus:border-primary"
            />
          </div>
          <div id="eng_rep-file-upload">
            <label className="mb-3 block text-black dark:text-white">
              Attach Engineering Report
            </label>
            <input
              onChange={handleFileChange}
              type="file"
              multiple
              ref={engRef}
              className="w-full cursor-pointer rounded-lg border-[1.5px] border-stroke bg-transparent outline-none transition file:mr-5 file:border-collapse file:cursor-pointer file:border-0 file:border-r file:border-solid file:border-stroke file:bg-whiter file:py-3 file:px-5 file:hover:bg-primary file:hover:bg-opacity-10 focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:file:border-form-strokedark dark:file:bg-white/30 dark:file:text-white dark:focus:border-primary"
            />
          </div>
        </div>
        <div className="p-6.5">
          <button
            type="submit"
            className="inline-flex rounded bg-silas-dark px-3 py-1 font-medium text-white hover:bg-opacity-90 sm:px-6 sm:py-2.5"
          >
            Save Submission
          </button>
        </div>
      </form>
    </div>
  );
};

export default SubmissionForm;
