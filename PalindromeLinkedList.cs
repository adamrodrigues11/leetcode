/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public bool IsPalindrome(ListNode head) {
        Stack<int> observed = new Stack<int>();
        ListNode fast = head;
        ListNode slow = head;
        while ( slow != null ) {
            if (fast != null ) {
                fast = fast.next;
                if ( fast != null ) {
                    fast = fast.next;
                    observed.Push(slow.val);
                    slow = slow.next;
                } else {
                    // first time fast reaches end with odd # of nodes
                    observed.Push(slow.val);
                }
            } else {
                // first time fast reaches end with even # of nodes, and every time after before slow reaches end
                if ( observed.Peek() == slow.val ) {
                    observed.Pop();
                    slow = slow.next;
                } else {
                    return false;
                }
            }            
        }
        return true;
    }
}

/* 
Pretty much implemented the same solution as the MiddleLinkedList.cs, 
but added the slowly traversed node values to a stack while the fast node traversed the list.
Then, when the fast node reached the end, the slow node was at the middle, and we could compare the top of the stack
to the slow node's value. If they were equal, we pop the stack and continue traversing the list. If not, we return false.
*/