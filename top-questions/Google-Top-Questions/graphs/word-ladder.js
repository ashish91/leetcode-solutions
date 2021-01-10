/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */

let oneCharacterDiff = (str1, str2) => {
  let diffCharCount = 0;

  for (let i = 0; i < str1.length; i++) {
    if (str1[i] !== str2[i]) {
      diffCharCount += 1;
    }

    if (diffCharCount > 1) {
      return false;
    }
  }

  return true;
}

let buildGraph = (words) => {
  let graph = {};
  for (let i = 0; i < words.length; i++) {
    for (let j = i+1; j < words.length; j++) {
      if (oneCharacterDiff(words[i], words[j])) {
        graph[words[i]] = graph[words[i]] || [];
        graph[words[i]].push(words[j]);

        graph[words[j]] = graph[words[j]] || [];
        graph[words[j]].push(words[i]);
      }
    }
    graph[words[i]] = [...new Set(graph[words[i]])];
  }

  return graph;
}

var ladderLength = function(beginWord, endWord, wordList) {
  if (!wordList.includes(endWord)) {
    return 0;
  }

  let graph = buildGraph(wordList.concat([beginWord, endWord]));

  let queue = [beginWord], currentNodes, neighbours, visited = {};
  let ladder = 0;
  while (queue.length > 0) {
    ladder += 1;
    currentNodes = queue;
    queue = [];

    for (i = 0; i < currentNodes.length; i++) {
      if (!visited[currentNodes[i]]) {
        if (currentNodes[i] == endWord) {
          return ladder;
        }

        visited[currentNodes[i]] = true;
        queue = queue.concat(graph[currentNodes[i]]);
      }
    }
  }

  return 0;
};
