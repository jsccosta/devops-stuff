import { useEffect, useState } from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';

import Loader from './common/Loader';
import PageTitle from './components/PageTitle';
import Dashboard from './pages/Dashboard/Main';

// import 'silastic/styles/tailwind.css';



import Settings from './pages/Settings';
// import Settings from './pages/Settings';
// some comment
import DocumentViewer from './pages/DocumentViewer/DocumentViewer'
import Accounts from './pages/Accounts/Main';
import Submissions from './pages/Submissions/Main'
import AccountDetails from './pages/Accounts/AccountDetails/Main';
import SubmissionDetail from './pages/Submissions/SubmissionDetail';
import EngineeringReports from './pages/EngineeringReports/EngineeringReports';

import Callback from './pages/Callback';
import RequireAuth from './RequireAuth';

import ChatBot from './components/Chatbox';

function App() {
  const [loading, setLoading] = useState<boolean>(true);
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  useEffect(() => {
    setTimeout(() => setLoading(false), 1000);
  }, []);

  return loading ? (
    <Loader />
  ) : (
    <>
    <ChatBot />
      <Routes>
      <Route
          index
          element={
            <>
              <PageTitle title="Silas Insurtech" />
              <Dashboard />
            </>
          }
        />
        <Route path="/callback" element={<Callback />} />
        <Route path="/protected" element={<RequireAuth />}>
 
        </Route>
        <Route
          path="/accounts"
          element={
            <>
              <PageTitle title="Accounts - Silas Insurtech" />
              <Accounts />
            </>
          }
        />
        <Route
          path="/engineering"
          element={
            <>
              <PageTitle title="Engineering Reports - Silas Insurtech" />
              <EngineeringReports />
            </>
          }
        />
        <Route
          path="/submissions"
          element={
            <>
              <PageTitle title="Submissions - Silas Insurtech" />
              <Submissions />
            </>
          }
        />
        <Route
          path="/accounts/:accountId"
          element={
            <>
              <PageTitle title="Accounts details - Silas Insurtech" />
              <AccountDetails />
            </>
          }
        />
        <Route
          path="/submission/:submissionId"
          element={
            <>
              <PageTitle title="Submission details - Silas Insurtech" />
              <SubmissionDetail />
            </>
          }
        />
        <Route
          path="/settings"
          element={
            <>
              <PageTitle title="Settings - Silas Insertech" />
              <Settings />
            </>
          }
        />
        <Route
          path="/document-viewer"
          element={
            <>
              <PageTitle title="Document Comparison - Silas Insertech" />
              <DocumentViewer />
            </>
          }
        />
      </Routes>
    </>
  );
}

export default App;
