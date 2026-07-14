class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return; // No need to return head since method is void
        }

        // Step 1: Find the middle using slow-fast pointer approach
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Step 2: Reverse the second half of the list
        ListNode prev = null, current = slow, temp;
        while (current != null) {
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }

        // Step 3: Merge the two halves alternately
        ListNode first = head, second = prev;
        while (second.next != null) { // Merge till second half is exhausted
            temp = first.next;
            first.next = second;
            first = temp;

            temp = second.next;
            second.next = first;
            second = temp;
        }
    }
}
