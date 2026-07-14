class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;

        // Step 1: Find the length of the linked list
        int length = 0;
        ListNode current = head;
        while (current != null) {
            length++;
            current = current.next;
        }

        // Step 2: If we need to remove the head node
        if (n == length) {
            return head.next;
        }

        // Step 3: Find the (length - n)th node
        current = head;
        for (int i = 1; i < length - n; i++) {
            current = current.next;
        }

        // Step 4: Remove the nth node from end
        current.next = current.next.next;

        return head;
    }
}
