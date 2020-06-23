/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
let bfs = function(source, target, deadends) {
  let queue = [source, null];

  let visited = {};
  visited[source] = true;

  let depth = 0;
  while (queue.length > 0) {
    let current = queue.shift();

    if (current == null) {
      depth += 1;
      if (queue[0] != null) {
        queue.push(null);
      }
    } else if (current == target) {
      return depth;
    } else if (!deadends.includes(current)) {
      let directions = [-1, 1];
      for (let i = 0; i < current.length; i++) {
        for (let d in directions) {
          let next = (parseInt(current[i]) + directions[d] + 10) % 10;
          let nextLock = current.substring(0, i) + next + current.substring(i+1, current.length);

          if (!visited[nextLock]) {
            visited[nextLock] = true;
            queue.push(nextLock);
          }
        }
      }
    }
  }

  return -1;
}

var openLock = function(deadends, target) {
  return bfs('0000', target, deadends);
};
