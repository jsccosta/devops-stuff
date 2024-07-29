import { ChangeEvent, Dispatch, SetStateAction, FormEvent, ReactNode } from 'react';

import { useState } from 'react';
import axios from 'axios';

import FileUpload from './FileUpload';

type FilesUploaderProps = {
  setRequestSuccess: Dispatch<SetStateAction<boolean>>;
  setComparedDocument: Dispatch<SetStateAction<File | null>>;
  setOriginalDocument: Dispatch<SetStateAction<File | null>>;
  setRecentDocument: Dispatch<SetStateAction<File | null>>;
};

type FileState = File | null;
type FileNameState = string | null;

// Define the props for the form component
interface FormProps {
  onSubmit: (event: FormEvent<HTMLFormElement>) => void;
  children: ReactNode;
}

// Define the form component
const Form: React.FC<FormProps> = ({ onSubmit, children }) => {
  return <form onSubmit={onSubmit}>{children}</form>;
};

const FilesUploader: React.FC<FilesUploaderProps> = ({
  setRequestSuccess,
  setComparedDocument,
  setOriginalDocument,
  setRecentDocument,
}) => {
  const [file1, setFile1] = useState<FileState>(null);
  const [file1Name, setFile1Name] = useState<FileNameState>(null);

  const [file2, setFile2] = useState<FileState>(null);
  const [file2Name, setFile2Name] = useState<FileNameState>(null);

  const handleFile1Change = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setFile1(file);
      setFile1Name(file.name);
    }
  };

  // Function to handle file input change for the second file
  const handleFile2Change = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setFile2(file);
      setFile2Name(file.name);
    }
  };

  // Function to handle form submission
  const handleSubmit = async (event: FormEvent<HTMLFormElement>): Promise<void> => {
    event.preventDefault();

    // Create FormData object and append files
    const formData = new FormData();

    formData.append('previous_document_version', file1, 'v1-doc.pdf');
    formData.append('current_document_version', file2, 'v2-doc.pdf');

    // ToDo: Change endpoint URL
    try {
      const response = await axios.post(
        '/api/v1/upload/',
        formData,
        {
          headers: {
            accept: 'application/json',
            'Content-Type': 'multipart/form-data',
          },
        },
      );
      if (response.status === 200) {
        setComparedDocument(response.data.parsedFiles);
        setOriginalDocument(response.data.filepaths.original_file);
        setRecentDocument(response.data.filepaths.new_file);
        setRequestSuccess(true);
      }
      console.log('Upload successful:', response.data);
    } catch (error) {
      console.error('Upload failed:', error);
    }
  };

  return (
    <div>
      <h2>Upload documents for comparison</h2>
      <Form onSubmit={handleSubmit}>
        <FileUpload
          label={'File 1'}
          file={file1Name}
          onChangeHandler={handleFile1Change}
        />
        <FileUpload
          label={'File 2'}
          file={file2Name}
          onChangeHandler={handleFile2Change}
        />
        <button
          className="mt-3 inline-flex rounded bg-primary px-3 py-1 font-medium text-white hover:bg-opacity-90 sm:px-6 sm:py-2.5"
          type="submit"
        >
          Upload
        </button>
      </Form>
    </div>
  );
};

export default FilesUploader;
