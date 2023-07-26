"""
** Maximum Depth of Binary Tree **
Given a binary tree, find its maximum depth.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


# Test Cases
# root = [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(max_depth(root))

# root = [1,null,2]

root_2 = TreeNode(1)
root_2.right = TreeNode(2)

print(max_depth(root_2))
