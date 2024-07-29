import { useLogto } from '@logto/react';
import { useEffect } from 'react';
import { Outlet } from 'react-router-dom';

// import { redirectUrl } from './consts';

export const baseUrl = window.location.origin;
export const redirectUrl = `${baseUrl}/callback`;

export const appId = 'sampleId'; // Register the sample app in Logto dashboard
export const endpoint = 'http://localhost:3001'; // Replace with your own Logto endpoint

const RequireAuth = () => {
  const { isAuthenticated, isLoading, signIn } = useLogto();

  useEffect(() => {
    if (!isAuthenticated && !isLoading) {
      void signIn(redirectUrl);
    }
  }, [isAuthenticated, isLoading, signIn]);

  return isAuthenticated ? <Outlet /> : <p>Not authenticated</p>;
};

export default RequireAuth;