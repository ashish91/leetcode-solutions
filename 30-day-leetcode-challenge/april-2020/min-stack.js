/**
 * initialize your data structure here.
 */
var MinStack = function() {
  this.stack = [];
  this.minTracker = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
  if (this.minTracker.length == 0 || x <= this.getMin()) {
    this.minTracker.push(x);
  }
  this.stack.push(x);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  if (this.getMin() == this.top()) {
    this.minTracker.pop();
  }
  this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.stack[this.stack.length-1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
  return this.minTracker[this.minTracker.length-1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
