"""
Runtime: 28 ms, faster than 91.90% of Python3 online submissions for Sort Colors.
Memory Usage: 14 MB, less than 35.12% of Python3 online submissions for Sort Colors.
https://youtu.be/XOX1WvUMpwQ?t=1114
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, left, right = 0,0,len(nums)-1
        while left<=right:
            if nums[left]==0:
                nums[left], nums[p0]=nums[p0],0
                p0+=1
                left+=1
            elif nums[left]==2:
                nums[left],nums[right]=nums[right],2
                right-=1
            else:
                left+=1
