export function formatToDollar(number) {
    return number.toLocaleString('en-US', { style: 'currency', currency: 'USD',
    minimumFractionDigits: 0,
  maximumFractionDigits: 0
  });
  }

  export function formatToPercent(number) {
    return (number * 100).toLocaleString('en-US', { style: 'percent' });
  }

  export function naivePercent(string){
    return `${string.toFixed(2)} %`
  }