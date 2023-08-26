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

  // First solution - O(1.5 * n) time as we traverse the list to find the length, 
 // and then halfway again to its middle node
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        ListNode n = head;
        short length = 1;
        while ( n.next != null ) {
            n = n.next;
            length++;
        }
        n = head;
        short i = 0;
        while ( i < length / 2 ) {
            n = n.next;
            i++;
        }
        return n;
    }
}

// This solution only traverses the linkedlist once, and stores each pointer in an array of pointers as we go
 // Although it uses more memory than the other solution, it reduces time complexity to O(n) as the final step is
 // looking up the pointer of the middle node by index O(1), instead of traversing half the list again 
 // ends up being slower though becase of the extra comparison (and memory allocation?)
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        ListNode n = head;
        short length = 1;
        var pointers = new ListNode[51]; // can have at most 100 nodes in the linkedlist, only need pointers to middle +1 
        pointers[0] = head; // put outside of loop for base case of 1 node in linkedlist
        while ( n.next != null ) {
            n = n.next;
            length++;
            if ( length <= 51 ) { 
                pointers[length - 1] = n;
            }
        }
        return pointers[length / 2];
    }
}

// Fastest solution - use a fast node and slow node (at half speed) to traverse the list once together
// When the fast node reaches the end, the slow node will be at the middle
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while ( fast != null && fast.next != null ) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}