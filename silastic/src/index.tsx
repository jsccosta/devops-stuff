import React, { FC, HTMLAttributes, ReactChild } from 'react';


export interface ThingProps extends HTMLAttributes<HTMLDivElement> {
  /** custom content, defaults to 'the snozzberries taste like snozzberries' */
  children?: ReactChild;
}

export const Thing: FC<ThingProps> = ({ children }) => {
  return (
    <div className="bg-yellow-100 mt-10 p-5 rounded-md">
      {children || `the snozzberries taste like snozzberries do`}
    </div>
  );
};