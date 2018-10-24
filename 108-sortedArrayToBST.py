# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        root = self.constructBST(nums)
        return root
        
    def constructBST(self, nums):
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.constructBST(nums[0:mid])
        node.right = self.constructBST(nums[mid+1:len(nums)])
        return node