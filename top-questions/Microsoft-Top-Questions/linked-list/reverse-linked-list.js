/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
let reverseHead = null

let recursiveReverse = function(node) {
  if (node == null) {
    return node;
  }
  else if (node.next == null) {
    reverseHead = node;
    return node
  }

  let next = recursiveReverse(node.next);
  next.next = node;
  node.next = null;
  return node;
}

let reverseList = function(head) {
  reverseHead = null;
  recursiveReverse(head);
  return reverseHead;
};
