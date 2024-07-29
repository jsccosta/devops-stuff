import { ReactNode } from "react";

interface TabProps{
  label: string;
  children: ReactNode;
}

const Tab: React.FC<TabProps> = ({ label, children }) => {
  return (
    <div data-label={label} className="hidden">
      {children}
    </div>
  );
};

export default Tab;