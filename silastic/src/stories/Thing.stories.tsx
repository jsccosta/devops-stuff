// import React from 'react';
// import { Meta, Story } from '@storybook/react';
// import { Thing, Props } from '../src';

// const meta: Meta = {
//   title: 'Welcome',
//   component: Thing,
//   argTypes: {
//     children: {
//       control: {
//         type: 'text',
//       },
//     },
//   },
//   parameters: {
//     controls: { expanded: true },
//   },
// };

// export default meta;

// const Template: Story<Props> = args => <Thing {...args} />;

// // By passing using the Args format for exported stories, you can control the props for a component for reuse in a test
// // https://storybook.js.org/docs/react/workflows/unit-testing
// export const Default = Template.bind({});

// Default.args = {};


import type { Meta, StoryObj } from '@storybook/react';
import { fn } from '@storybook/test';
import {Thing, ThingProps } from '../index'

// More on how to set up stories at: https://storybook.js.org/docs/writing-stories#default-export
const meta: Meta = {
  title: 'Example/Thing',
  component: Thing,
  parameters: {
    // Optional parameter to center the component in the Canvas. More info: https://storybook.js.org/docs/configure/story-layout
    // layout: 'centered',
  },
  // This component will have an automatically generated Autodocs entry: https://storybook.js.org/docs/writing-docs/autodocs
//   tags: ['autodocs'],
  // More on argTypes: https://storybook.js.org/docs/api/argtypes
  argTypes: {
        children: {
      control: {
        type: 'text',
      },
    },
  },
  // Use `fn` to spy on the onClick arg, which will appear in the actions panel once invoked: https://storybook.js.org/docs/essentials/actions#action-args
//   args: { onClick: fn() },
};

export default meta;
type Story = StoryObj<ThingProps>;

export const Primary: Story = {};

