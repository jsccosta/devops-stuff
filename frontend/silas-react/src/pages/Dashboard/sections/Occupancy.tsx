import React, { useState, useEffect } from 'react';

import Table from '../../../components/Tables/Table';
import BarChartComponent from '../../../components/Charts/BarChartComponent';

import { formatToDollar, naivePercent } from '../../../utils/formatters';

import axios from 'axios';

import { accountsOccupancyGeneral } from '../dummy-data';

import { chartOptions } from '../chart-configs';

const columns = [
  { Header: 'Occupancy', accessor: 'occupancy' },
  { Header: 'ISO Number', accessor: 'iso' },
  {
    Header: 'GWP',
    accessor: 'gwp',
    Cell: ({ value }) => `${formatToDollar(value)}`,
  },
  {
    Header: 'TIV',
    accessor: 'tiv',
    Cell: ({ value }) => `${formatToDollar(value)}`,
  },
  {
    Header: 'Average Base Rate %',
    accessor: 'base_rate',
    Cell: ({ value }) => `${naivePercent(value)}`,
  },
  {
    Header: 'Claims Total (USD)',
    accessor: 'claims_total',
    Cell: ({ value }) => `${formatToDollar(value)}`,
  },
  {
    Header: 'Loss Ratio %',
    accessor: 'loss_ratio',
    Cell: ({ value }) => `${naivePercent(value)}`,
  },
];

const Toggler = ({ items, onClickHandler }) => {
  const [activeView, setActiveView] = useState(items[0].label);

  return (
    <>
      <div className="flex border-b border-gray-300 w-1/2">
        {items.map((label) => {
          return (
            <button
              key={label.id}
              className={`${
                activeView === label.label ? 'border-b-2 border-purple-500' : ''
              } flex-1 text-gray-700 font-medium py-2`}
              onClick={(e) => {
                e.preventDefault();
                setActiveView(e.target.textContent);
                onClickHandler(e.target.textContent);
              }}
            >
              {label.label}
            </button>
          );
        })}
      </div>
    </>
  );
};

const togglerItems = [
  {
    id: 'general',
    label: 'General View',
  },
  {
    id: 'detailed',
    label: 'Detailed View',
  },
];
const Occupancy: React.FC = () => {
  const [depOccupancy, setDepOccupancy] = useState(null);
  const [activeView, setActiveView] = useState(togglerItems[0].label);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [dep_occupancy] = await Promise.all([
          axios.get('/api/v1/department_occupancy/'),
        ]);
        setDepOccupancy(dep_occupancy.data.department_occupancy);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div id="occupancy-split" className="relative w-full my-4 border-b pb-4">
      <div className="w-full mb-4">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-title-md2 font-semibold text-black dark:text-white">
            Occupancy Split
          </h2>
          <Toggler
            items={togglerItems}
            onClickHandler={(selectedView) => setActiveView(selectedView)}
          />
        </div>
        {activeView === togglerItems[0].label ? (
          <div className="py-4">
            <div id="table_wrapper" className="bg-white">
              {depOccupancy ? (
                <Table
                  columns={columns}
                  data={depOccupancy}
                />
              ) : null}
            </div>
          </div>
        ) : (
          <div className="py-4">
            <div className="py-4">
              <BarChartComponent
                options={chartOptions}
                label={''}
                series={accountsOccupancyGeneral.series}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Occupancy;
