import React from 'react';
import { useTable } from 'react-table';
import { useNavigate } from 'react-router-dom';
import { Tooltip } from 'react-tooltip';

const Table: React.FC = ({
  columns: userColumns,
  data,
  extraProps,
  rowClickHandler,
  actions,
  actionWrapperClass=''
}) => {
  const navigate = useNavigate();

  // const handleClick = (row) => {
  //   const companyId = row.values.company_id;

  //   navigate(`/accounts/${companyId}`);
  // };

  const columns = React.useMemo(() => {
    const actionColumn = actions      ? [
          {
            Header: 'Actions',
            id: 'actions',
            Cell: ({ row }) => (
              <div className={actionWrapperClass}>
                {actions.map((action) => (
                  <button
                    id={action.label}
                    key={action.label}
                    onClick={() => action.onClick(row.original)}
                  >
                    {action.icon ? action.icon : action.label}
                    {action.tooltip ?
                    
                    <Tooltip id="table-tooltip" anchorSelect={`#${action.label}`} place="top">
                      {action.tooltip}
                    </Tooltip>
                    : null}
                  </button>
                ))}
              </div>
            ),
          },
        ]
      : [];

    return [...userColumns, ...actionColumn];
  }, [actions, userColumns]);

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable({ columns, data, initialState: { ...extraProps } });

  return (
    <div className="flex flex-col relative overflow-x-auto shadow-md sm:rounded-lg py-8">
      <div className="relative flex ml-4">
        <div className="mb-4 bg-white dark:bg-gray-900">
          <input
            type="text"
            id="floating_outlined"
            className="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-blue-500 dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" "
          />
          <div className="flex items-center absolute peer-focus:px-2 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-6 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">
            <svg
              className="w-4 h-4 text-gray-500 dark:text-gray-400 mr-1"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
            <label
              htmlFor="floating_outlined"
              className="text-sm text-gray-500 dark:text-gray-400 duration-300  scale-75 z-10 origin-[0] bg-white dark:bg-gray-900 px-2 py-1"
            >
              Search...
            </label>
          </div>
        </div>
      </div>
      <table {...getTableProps()} className="table-auto w-full">
        {/* <thead className='bg-gray-50 dark:bg-gray-700 dark:text-gray-400'> */}
        <thead className="bg-blue-100">
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th {...column.getHeaderProps()} className="px-4 py-2 ">
                  {column.render('Header')}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {rows.length > 0 ? (
            rows.map((row) => {
              prepareRow(row);
              return (
                <tr
                  {...row.getRowProps()}
                  onClick={() => {
                    rowClickHandler ? rowClickHandler(row) : null;
                  }}
                  className={`${
                    rowClickHandler ? 'hover:cursor-pointer ' : ''
                  }bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600`}
                >
                  {row.cells.map((cell) => {
                    const cellContent = cell.value;
                    const isNumber = !isNaN(Number(cellContent));
                    return (
                      <td
                        {...cell.getCellProps()}
                        className={`w-4 p-4 ${isNumber ? 'text-right' : 'text-left'}`}
                      >
                        {cell.render('Cell')}
                      </td>
                    );
                  })}
                </tr>
              );
            })
          ) : (
            <tr>
              <td
                className="p-8 text-center bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                colSpan={columns.length}
              >
                No data available
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
