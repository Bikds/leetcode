# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: [ListNode]) -> bool:

    p1 = head
    p2 = head

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


    # l = set()
    # while head:
    #     if head in l:
    #         return True
    #     else:
    #         l.add(head)
    #
    #     head = head.next
    #
    # return False







if __name__ == "__main__":
