# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
# def convert(num):
#     if num == "I":
#         return 1
#     elif num == "V":
#         return 5
#     elif num == "X":
#         return 10
#     elif num == "L":
#         return 50
#     elif num == "C":
#         return 100
#     elif num == "D":
#         return 500
#     elif num == "M":
#         return 1000
#
#
# def romanToInt(s):
#     num = 0
#     idx = 0
#     length = len(s)
#     skip_last = False
#     subtraction_list = ["IV", "IX", "XL", "XC", "CD", "CM"]
#     while idx < length - 1:
#         # print(s[idx:idx+2])
#         if s[idx:idx+2] in subtraction_list:
#             # print("here")
#             # print(convert(s[idx+1]))
#             # print(convert(s[idx]))
#             num += convert(s[idx+1]) - convert(s[idx])
#             skip_last = (idx + 1 == length - 1)
#             idx += 2
#         else:
#             num += convert(s[idx])
#             idx += 1
#
#     if not skip_last:
#         num += convert(s[length - 1])
#
#     return num
#
# print(romanToInt("IV"))
# print(romanToInt("XI"))
# print(romanToInt("XIV"))
# print(romanToInt("XVII"))

from binarytree import Node

class Queue:
    """
    A simple implementation of a FIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        # uses a list as the basis for the queue
        # initializes Queue object to an empty list
        self._queue = []

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        # returns the length of queue by using list object's len function
        return len(self._queue)

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        # concatenates list elements to to_string and separates elements
        # with a space
        to_string = ""
        for element in self._queue:
            to_string += str(element) + " "
        return to_string

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        # adds the pushed item to the end of queue
        self._queue.append(item)

    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        # pops the first element (since FIFO)
        return self._queue.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        # replaces queue with an empty list, essentially "clearing" queue
        self._queue = []


def level_with_highest_sum(root) -> int:
    # Since the children of each node can be at most half of the parent, the sum of the children will be less than or equal to the parent.
    # However when the sum of the two children is equal to the parent, the level needs to reflect the level of the children.
    # So, we will use a breadth first search which terminates when any of the children is not half of the parents value

    # initializing level to 1
    level = 1
    queue = []
    queue.append(root)

    while True:
        queue_next = []
        for node in queue:
            if node.left is None or node.right is None:
                return level
            elif node.left.value != node.right.value or 2 * node.left.value != node.value:
                return level
            else:
                queue_next.append(node.left)
                queue_next.append(node.right)
                queue.remove(node)
        queue = queue_next
        level += 1

bt = Node(24)
bt.left = Node(8)
bt.right = Node(4)
print(bt)