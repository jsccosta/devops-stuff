import React, { useState } from 'react';

const FileUploadForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
    files: null,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleFileChange = (e) => {
    const files = e.target.files;
    setFormData({
      ...formData,
      files: files,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const { name, email, message, files } = formData;

    // You can perform form validation here

    // Prepare form data to be sent
    const formDataToSend = new FormData();
    formDataToSend.append('name', name);
    formDataToSend.append('email', email);
    formDataToSend.append('message', message);
    if (files) {
      for (let i = 0; i < files.length; i++) {
        formDataToSend.append('files', files[i]);
      }
    }

    // Send formDataToSend to the server using fetch or Axios
    // Example:
    // fetch('/submit-form', {
    //   method: 'POST',
    //   body: formDataToSend,
    // })
    // .then(response => response.json())
    // .then(data => console.log(data))
    // .catch(error => console.error('Error:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="message">Message:</label>
        <textarea
          id="message"
          name="message"
          value={formData.message}
          onChange={handleChange}
        ></textarea>
      </div>
      <div>
        <label htmlFor="files">Upload Files:</label>
        <input
          type="file"
          id="files"
          name="files"
          multiple
          onChange={handleFileChange}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default FileUploadForm;
