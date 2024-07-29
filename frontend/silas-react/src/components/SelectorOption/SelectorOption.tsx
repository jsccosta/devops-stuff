
export interface OptionType{
    id: string | number;
    label: string;
}

interface SelectorOptionTypes{
    option: OptionType
}

const SelectorOption: React.FC<SelectorOptionTypes> = ({ option }) => {
  return (
    <option value={option.id} className="text-body dark:text-bodydark">
      {option.label}
    </option>
  );
};

export default SelectorOption;
