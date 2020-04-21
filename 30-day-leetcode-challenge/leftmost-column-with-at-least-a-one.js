/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * function BinaryMatrix() {
 *     @param {integer} x, y
 *     @return {integer}
 *     this.get = function(x, y) {
 *         ...
 *     };
 *
 *     @return {[integer, integer]}
 *     this.dimensions = function() {
 *         ...
 *     };
 * };
 */

/**
 * @param {BinaryMatrix} binaryMatrix
 * @return {number}
 */
var leftMostColumnWithOne = function(binaryMatrix) {
  let size = binaryMatrix.dimensions();
  let row = 0;
  let col = size[1] - 1;

  while (row < size[0] && col >= 0) {
    if (binaryMatrix.get(row, col) == 1) {
      col -= 1;
    } else if (binaryMatrix.get(row, col) == 0) {
      row += 1;
    }
  }

  if (col == size[1] - 1) {
    return -1;
  } else {
    return col + 1;
  }
};
