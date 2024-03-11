# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(l, r):
            return None if l > r else [mid:=(l+r)//2, TreeNode(nums[mid], bst(l, mid-1), bst(mid+1, r))][1]

        return bst(0, len(nums)-1)
