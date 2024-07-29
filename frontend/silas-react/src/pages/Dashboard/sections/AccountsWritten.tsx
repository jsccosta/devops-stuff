import React from 'react';

import { Tabs, Tab } from '../../../components/Tabs';
import BarChartComponent from '../../../components/Charts/BarChartComponent';

import {
  accountsWrittenPremiumMonth,
  accountsWrittenMonth,
  sideBySideBarChartProps
} from '../dummy-data';

import { acctsWrittenMonthOptions, stackedOptions } from '../chart-configs';

const AccountsWritten: React.FC = () => {
  return (
    <div id="occupancy-split" className="relative w-full my-4 border-b pb-4">
      <div className="w-full mb-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-title-md2 font-semibold text-black dark:text-white">
            Accounts Written
          </h2>
        </div>
        <div className="py-4">
          <Tabs>
            <Tab label="By Month">
              <div className="py-4">
                <BarChartComponent
                  options={acctsWrittenMonthOptions}
                  series={accountsWrittenMonth.series}
                />
              </div>
            </Tab>
            <Tab label="Premium by Month - 2022 to 2023">
              <div className="py-4">
                <BarChartComponent
                  options={sideBySideBarChartProps}
                  series={accountsWrittenPremiumMonth.series}
                />
              </div>
            </Tab>
          </Tabs>
        </div>
      </div>
    </div>
  );
};

export default AccountsWritten;
