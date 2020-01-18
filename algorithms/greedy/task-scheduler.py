class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    taskCounts = {}
    maxTask = 0
    maxTaskCount = 0

    for task in tasks:
      if task in taskCounts:
        taskCounts[task] += 1
      else:
        taskCounts[task] = 1

      if maxTask == taskCounts[task]:
        maxTaskCount += 1
      elif maxTask < taskCounts[task]:
        maxTask = taskCounts[task]
        maxTaskCount = 1

    windowCount = maxTask - 1
    emptySlots = windowCount * (n - (maxTaskCount - 1)) # 2 * (2 - (2 - 1))
    availableTasks = len(tasks) - (maxTask * maxTaskCount) # 6 - (3 * 2) = 0
    idles = max(0, emptySlots - availableTasks)

    return len(tasks) + idles
