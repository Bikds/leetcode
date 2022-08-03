class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int):

    temp = ListNode()
    temp.next = head

    while temp.next:
        if temp.next.val == val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
