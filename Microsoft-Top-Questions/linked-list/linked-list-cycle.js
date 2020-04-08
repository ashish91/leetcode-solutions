/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
  if (!head) {
    return false;
  }

  let slow = head, fast = head.next;
  while (fast != null && fast.next != null) {
    if (fast == slow) {
      return true;
    }

    fast = fast.next.next;
    slow = slow.next;
  }

  return false;
};
