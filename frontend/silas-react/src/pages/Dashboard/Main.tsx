import React from 'react';

import Layout from '../../layout/Layout';
import { useLogto, type UserInfoResponse } from '@logto/react';
import { useEffect, useState } from 'react';

import TargetBar from './sections/TargetBar';
import PortfolioOverview from './sections/PortfolioOverview';
import GrossClaims from './sections/GrossClaims'
import Occupancy from './sections/Occupancy';
import AccountsWritten from './sections/AccountsWritten';
import TotalInsuredValue from './sections/TotalInsuredValue';
// import {Thing} from '../../silastic/dist/index.js'

// import {Thing} from 'silastic';

// import {Thing} from '../../../../silastic/dist/index'

import MapComponent from './MapComponent/Map';

export const baseUrl = window.location.origin;
export const redirectUrl = `${baseUrl}/callback`;

export const appId = 'sampleId'; // Register the sample app in Logto dashboard
export const endpoint = 'http://localhost:3001'; // Replace with your own Logto endpoint
import { LONDON } from '../../map_data/london';


const Dashboard: React.FC = () => {
  const { isAuthenticated, signIn, signOut, fetchUserInfo } = useLogto();
  const [user, setUser] = useState<UserInfoResponse>();

  useEffect(() => {
    (async () => {
      if (isAuthenticated) {
        const userInfo = await fetchUserInfo();
        setUser(userInfo);
      }
    })();
  }, [fetchUserInfo, isAuthenticated]);


  console.log({
    isAuthenticated,
    user
  })

  return (
    <>
    {/* <h3>Logto React sample</h3>
    {!isAuthenticated && (
      <>
        <button
          type="button"
          onClick={() => {
            void signIn(redirectUrl);
          }}
        >
          Sign in
        </button>
        <button
          type="button"
          onClick={() => {
            void signIn(redirectUrl, 'signUp');
          }}
        >
          Sign up
        </button>
      </>
    )}
    {isAuthenticated && (
      <button
        type="button"
        onClick={() => {
          void signOut(baseUrl);
        }}
      >
        Sign out
      </button>
    )} */}


    <Layout>
      {/* <Thing /> */}
      <TargetBar
        label={'Gross Written Premium vs. Target'}
        targetValue={'50'}
      />
      <PortfolioOverview />
      <AccountsWritten />
      <TotalInsuredValue />
      <GrossClaims />
      <Occupancy />
      <MapComponent mapData={LONDON} />
    </Layout>
    </>
  );
};

export default Dashboard;
