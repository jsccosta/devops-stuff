import React from 'react';
import ReactDOM from 'react-dom/client';
import { LogtoProvider, LogtoConfig } from '@logto/react';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';
import './css/style.css';
import './css/satoshi.css';
import 'flatpickr/dist/flatpickr.min.css';
// ToDo: load general css styles here


const config: LogtoConfig = {
  endpoint: 'http://localhost:3001/',
  appId: '989qces1pe25k34uuwehn',
};


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <LogtoProvider config={config}>
    <Router>
      <App />
    </Router>
    </LogtoProvider>
  </React.StrictMode>,
);
