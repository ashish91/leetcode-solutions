/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */

let computeSlope = function(point1, point2) {
  return (point2[1] - point1[1])/(point2[0] - point1[0]);
}

var checkStraightLine = function(coordinates) {
  let slope = computeSlope(coordinates[1], coordinates[0]);
  let currentSlope;

  for (let i = 2; i < coordinates.length; i++) {
    currentSlope = computeSlope(coordinates[i], coordinates[i-1]);
    if (slope != currentSlope) {
      return false;
    }
  }

  return true;
};
