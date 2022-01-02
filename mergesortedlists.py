def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    newLL = head

    while True:
        if l1 is None and l2 is None:
            break
        elif l1 is None:
            newLL = l2
            break
        elif l2 is None:
            newLL = l1
            break
        elif l1.val <= l2.val:
            newLL.next = l1
            l1 = l1.next
        else:
            newLL.next = l2
            l2 = l2.next
        newLL = newLL.next


    return head.next
