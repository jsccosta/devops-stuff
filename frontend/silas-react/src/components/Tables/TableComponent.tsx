interface tableDataRow {
  occupancy: string;
  gwp: string;
  tiv: string;
  isoNumber: string;
}

interface tableDataTypes {
  title: string;
  tableHeaders: string[];
  data: tableDataRow[];
}

const TableComponent: React.FC<tableDataTypes> = ({
  title,
  tableHeaders,
  data,
}) => {
  return (
    <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
      <div className="py-6 px-4 md:px-6 xl:px-7.5">
        <h4 className="text-sm text-black dark:text-white">{title}</h4>
      </div>
      <div className="grid grid-cols-6 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-8 md:px-6 2xl:px-7.5">
        {tableHeaders.map((tableHeader, idx) => {
          return (
            <div key={idx} className="col-span-2 flex items-center">
              <p className="font-medium">{tableHeader}</p>
            </div>
          );
        })}
      </div>
      {data.map((item, key) => (
        <div
          className="grid grid-cols-6 border-t border-stroke py-4.5 px-4 dark:border-strokedark sm:grid-cols-8 md:px-6 2xl:px-7.5"
          key={key}
        >
          <div className="col-span-2 hidden items-center sm:flex">
            <p className="text-sm text-black dark:text-white">
              {item.occupancy}
            </p>
          </div>
          <div className="col-span-2 hidden items-center sm:flex">
            <p className="text-sm text-black dark:text-white">{item.gwp}</p>
          </div>
          <div className="col-span-2 hidden items-center sm:flex">
            <p className="text-sm text-black dark:text-white">{item.tiv}</p>
          </div>
          <div className="col-span-1 flex items-center">
            <p className="text-sm text-black dark:text-white">
              {item.isoNumber}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default TableComponent;
