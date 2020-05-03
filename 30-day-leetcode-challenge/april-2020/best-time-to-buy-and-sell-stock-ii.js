/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  if (prices.length < 2) {
    return 0;
  }
  let holding = prices[0], profit = 0, i = 0;

  while (i < prices.length) {
    if (prices[i+1] - prices[i] < 0) {
      profit += Math.max(prices[i] - holding, 0);
      holding = prices[i+1];
    }
    i += 1;
  }

  profit += prices[i-1] - holding;
  return profit;
};
