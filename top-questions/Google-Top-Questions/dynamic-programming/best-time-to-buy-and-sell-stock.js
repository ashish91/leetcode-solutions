/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let min = prices[0];
  let profit = 0;

  for (let i = 0; i < prices.length; i++) {
    if (min > prices[i]) {
      min = prices[i];
    } else if (profit < prices[i] - min) {
      profit = prices[i] - min;
    }
  }

  return profit;
};
