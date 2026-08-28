# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []
        
        if p == None:
            if q == None:
                return True
            else:
                return False
        elif q == None:
            if p == None:
                return True
            else:
                return False


        def in_order_p(node, p_list):
            if node.left:
                in_order_p(node.left, p_list)
            else:
                p_list.append(None)
            p_list.append(node.val)
            if node.right:
                in_order_p(node.right, p_list)
            
        def in_order_q(node, q_list):
            if node.left:
                in_order_q(node.left, q_list)
            else:
                q_list.append(None)
            q_list.append(node.val)
            print(q_list)
            if node.right:
                in_order_q(node.right, q_list)
            
        print(p_list, q_list)
        in_order_p(p, p_list)
        in_order_q(q, q_list)
        return True if p_list == q_list else False