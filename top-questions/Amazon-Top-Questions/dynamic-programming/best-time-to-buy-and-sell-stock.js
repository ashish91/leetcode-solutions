/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let minprice = prices[0];
  let maxprofit = 0;

  for (let i = 0; i < prices.length; i++) {
    if (minprice > prices[i]) {
      minprice = prices[i];
    } else if (maxprofit < prices[i] - minprice) {
      maxprofit = prices[i] - minprice;
    }
  }

  return maxprofit;
};
