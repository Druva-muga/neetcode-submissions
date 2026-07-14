/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode current;
        current = l1;
        int power = 10;
        int num1=l1.val;
        int num2=l2.val;
        while(current.next!=null){
            current=current.next;
            num1 = num1 + (current.val)*power;
            power=power*10;
        }
        current = l2;
        power = 10;
        while(current.next!=null){
            current=current.next;
            num2 = num2 + (current.val)*power;
            power=power*10;
        }
        current.next=l1;
        int sum = num1+num2;
        System.out.println(sum);
        current = l2;
        current.val=sum%10;
        sum=sum/10;
        while(sum>=1 && current.next != null){
            current=current.next;
            current.val = sum%10;
            sum=sum/10;
        }
        current.next = null;
        return l2;
    }
}
