import { useState, ReactNode } from 'react';

interface TabsProps {
  children: ReactNode;
}

const Tabs: React.FC<TabsProps> = ({ children }) => {
  const [activeTab, setActiveTab] = useState<string>(
    (children as React.ReactElement<any>[])[0].props.label,
  );

  const handleClick = (
    e: React.MouseEvent<HTMLButtonElement>,
    newActiveTab: string,
  ) => {
    e.preventDefault();
    setActiveTab(newActiveTab);
  };

  return (
    <>
      <div className="flex border-b border-gray-300">
        {(children as React.ReactElement<any>[]).map((child) => (
          <button
            key={child.props.label}
            className={`${
              activeTab === child.props.label
                ? 'border-b-2 border-purple-500'
                : ''
            } flex-1 text-gray-700 font-medium py-2`}
            onClick={(e) => handleClick(e, child.props.label)}
          >
            {child.props.label}
          </button>
        ))}
      </div>
      <div className="py-4">
        {(children as React.ReactElement<any>[]).map((child) => {
          if (child.props.label === activeTab) {
            return <div key={child.props.label}>{child.props.children}</div>;
          }
          return null;
        })}
      </div>
    </>
  );
};

export default Tabs;
