# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if curr.val == p.val or curr.val == q.val:
                return curr
            if p.val < curr.val:
                if q.val > curr.val:
                    return curr
                else:
                    curr = curr.left
            elif curr.right.val > p.val:
                curr = curr.right
            else:
                return curr