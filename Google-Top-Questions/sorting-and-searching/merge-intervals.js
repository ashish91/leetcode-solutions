/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
let merge = (intervals) => {
  if (intervals.length < 2) {
    return intervals;
  }

  intervals.sort((a, b) => a[0] - b[0]);

  let first, second, merged = [];
  while (intervals.length > 1) {
    first = intervals.shift();
    second = intervals.shift();

     // [2,6], [0, 1]
    if (first[1] > second[1]) {
      let temp = first;
      first = second;
      second = temp;
    }


    // [1,6], [2,7]
    if (first[1] >= second[0]) {
      intervals.unshift([Math.min(first[0], second[0]), Math.max(first[1], second[1])]);
    } else {
      merged.push(first);
      intervals.unshift(second);
    }
  }

  merged.push(intervals[0]);
  return merged;
}
