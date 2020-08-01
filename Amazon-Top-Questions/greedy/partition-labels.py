class Solution:
  def partitionLabels(self, S: str) -> List[int]:
    lastIndexes = { c: i for i, c in enumerate(S) }

    currPartitionStart = 0
    currPartitionEnd = 0

    partitions = []
    for i, c in enumerate(S):
      currPartitionEnd = max(lastIndexes[c], currPartitionEnd)

      if currPartitionEnd == i:
        partitions.append(currPartitionEnd - currPartitionStart + 1)
        currPartitionStart = currPartitionEnd + 1

    return partitions