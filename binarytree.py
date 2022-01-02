class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def level_with_highest_sum(root: BinaryTree) -> int:
    # Since the children of each node can be at most half of the parent, the sum of the children will be less than or equal to the parent.
    # However when the sum of the two children is equal to the parent, the level needs to reflect the level of the children.
    # So, we will use a breadth first search which terminates when any of the children is not half of the parents value

    # initializing level to 1 and creating an empty list which stores the nodes of the current level
    level = 1
    queue = []
    # add the first node to the list
    queue.append(root)

    while True:
        # will house the next level's nodes
        queue_next = []
        # go through every node in queue
        for node in queue:
            # if the left or right node is null, then it is impossible for this level to offer the largest sum
            if node.left is None or node.right is None:
                return level
            # if each of the nodes aren't equal to half of the parent's value, it's impossible for this level to offer
            # the largest sum
            elif node.left.value != node.right.value or 2 * node.left.value != node.value:
                return level
            # if both the left and right are equal to half the parent's value, then put them in the queue to be
            # potentially looked at in the next level
            else:
                queue_next.append(node.left)
                queue_next.append(node.right)
                # remove the current node from queue since it has been looked at
                queue.remove(node)
        # advance to the next level (which is why queue becomes queue_next)
        queue = queue_next
        level += 1
