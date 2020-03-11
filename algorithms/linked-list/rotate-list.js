/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
  if (!head || !head.next) {
    return head;
  }

  let len = 1, temp = head;
  while (temp.next) {
    len++;
    temp = temp.next
  }
  temp.next = head;
  temp = head

  let tail = len - (k%len);
  let i = 1;
  while (i != tail) {
    temp = temp.next;
    i++;
  }
  head = temp.next;
  temp.next = null;

  return head;
};
