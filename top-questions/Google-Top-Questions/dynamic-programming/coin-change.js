var coinChange = function(coins, amount) {
  var mem = Array(coins.length).fill(0);

  for (var i = 0; i < coins.length; i++) {
    for (var j = coins[i]; j <= amount; j++) {
      mem[j] = min(mem[j], mem[j-coins[i]])
    }
  }

  return mem[amount]
};
