class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length;
        if (n == 0 || (n == 1 && lists[0] == null)) {
            return null;
        }

        ListNode l1, l2, head;
        head = lists[0];

        for (int i = 1; i < n; i++) {
            l1 = head;
            l2 = lists[i];

            // If head is null, take l2 directly
            if (l1 == null) {
                head = l2;
                continue;
            }

            // If l2 is null, skip merging
            if (l2 == null) continue;

            // Handle the case where l2's head needs to go before head
            if (l2.val < head.val) {
                ListNode temp = l2;
                l2 = l2.next;
                temp.next = head;
                head = temp;
                l1 = head;
            }

            // Merge in-place
            while (l1 != null && l2 != null) {
                if (l1.next == null) {
                    l1.next = l2;
                    break;
                }

                if (l1.next.val >= l2.val) {
                    ListNode temp = l2;
                    l2 = l2.next;

                    temp.next = l1.next;
                    l1.next = temp;
                    l1 = l1.next;
                } else {
                    l1 = l1.next;
                }
            }
        }

        return head;
    }
}
