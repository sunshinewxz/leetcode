/*
Initialize current node to dummy head of the returning list.
Initialize carry to 0.
Initialize p and q to head of l1 and l2 respectively.
	Loop through lists l1 and l2 until you reach both ends.
	Set x to node p's value. If p has reached the end of l1, set to 0.
	Set y to node q's value. If q has reached the end of l2, set to 0.
	Set sum = x + y + carry.
	Update carry = sum / 10.
	Create a new node with the digit value of (sum mod 10) and set it to current node's next, then advance current node to next.
	Advance both p and q.
Check if carry = 1, if so append a new node with digit 11 to the returning list.
Return dummy head's next node.

Take extra caution of the following cases:

Test case	Explanation
l1=[0,1]
l2=[0,1,2]	When one list is longer than the other.

l1=[]
l2=[0,1]	When one list is null, which means an empty list.

l1=[9,9]
l2=[1]   	The sum could have an extra carry of one at the end, which is easy to forget.
*/

public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}