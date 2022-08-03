def mergeTwoLists(list1, list2):
    # iterative
    # head = temp = ListNode(0)
    # while list1 and list2:
    #     if list1.val <= list2.val:
    #         temp.next = list1
    #         list1 = list1.next
    #     else:
    #         temp.next = list2
    #         list2 = list2.next
    #     temp = temp.next
    #
    # temp.next = list1 or list2
    # return head.next

    # recursive
    if not list1 or not list2:
        return list1 or list2
    elif list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2





