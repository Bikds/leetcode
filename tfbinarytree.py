class BinaryTree:
    def __init__(self, mark=True, left=None, right=None):
        self.mark = mark
        self.left = left
        self.right = right


def longest_path_len(root: BinaryTree) -> int:
    # returns the first value outputted from find_max_val, which is the length of the longest path
    path_length, node_included = find_max_val(root)
    return path_length

def find_max_val(node: BinaryTree):
    # output format: (int, int) -- returns the value along with whether the node is included (1) or not (0)
    # this is a recursive function
    # we look into the left and right sides of any node (if it exists)
    # then we look into the different cases as described below

    # if there is no node, then there's no length or inclusion of that node
    if node == None:
        return (0, 0)

    # finding maximum value and whether the current node is included in this path of the left and right node of the
    # current node
    val_left, left_included = find_max_val(node.left)
    val_right, right_included = find_max_val(node.right)

    # if the node is False then return the maximum between its left and right child
    if node.val == False:
        return (max(val_left, val_right), 0)
    # if the node is True, then look at the following possibilities
    else:
        # if both the left and the right child are true, then return the sum of the two values plus 1 as the longest
        # path (spanning the node and its left and right children)
        if left_included == 1 and right_included == 1:
            return (val_left + val_right + 1, 1)
        # if only the left is true then return either the path including the current and left child's path or the right
        # child's path, depending on which is greater
        elif left_included == 1 and right_included == 0:
            if val_left + 1 > val_right:
                return (val_left + 1, 1)
            return (val_right, 0)
        # if only the left is true then return either the path including the current and right child's path or the left
        # child's path, depending on which is greater
        elif left_included == 0 and right_included == 1:
            if val_right + 1 > val_left:
                return (val_right + 1, 1)
            return (val_left, 0)
        # if neither child is the true then find the maximum value between the right child's path, left child's path,
        # or the current node only
        else:
            max_val = max(val_left, val_right)
            if max_val > 1:
                return (max_val, 0)
            return (1, 1)