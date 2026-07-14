/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        HashMap <Node,Node> oldtonew = new HashMap<>();
        oldtonew.put(null,null);
        Node current = head;
        Node newl;
        while(current!=null){
            newl = new Node(current.val);
            oldtonew.put(current, newl);
            current = current.next;
        }
        current = head;
        while(current!=null){
            oldtonew.get(current).next = oldtonew.get(current.next);
            oldtonew.get(current).random = oldtonew.get(current.random);
            current = current.next;
        }
        current=head;
        return oldtonew.get(current);
    }
}
