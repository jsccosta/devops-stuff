import React, { ChangeEvent } from 'react';

interface FileUploadProps {
  label: string;
  file: string | null;
  onChangeHandler: (event: ChangeEvent<HTMLInputElement>) => void;
}

const FileUpload: React.FC<FileUploadProps> = ({ label, file, onChangeHandler }) => {
  return (
    <div>
      <label htmlFor="fileItem">{label}:</label>
      {file ? (
        <span>{file}</span>
      ) : (
        <div className="relative mb-5.5 block w-full cursor-pointer appearance-none rounded border border-dashed border-primary bg-gray px-4 py-4 dark:bg-meta-4 sm:py-7.5">
          <input
            className="absolute inset-0 z-50 m-0 h-full w-full cursor-pointer p-0 opacity-0 outline-none"
            type="file"
            id="fileItem"
            accept=".pdf,.doc,.docx"
            onChange={onChangeHandler}
          />
          <div className="flex flex-col items-center justify-center space-y-3">
            <p className="text-sm font-medium">
              <span className="text-primary">Click to upload</span> or drag and drop
            </p>
          </div>
        </div>
      )}
    </div>
  );
};


export default FileUpload;