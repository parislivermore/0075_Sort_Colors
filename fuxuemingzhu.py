个人博客： http://fuxuemingzhu.cn/

目录
题目描述
题目大意
解题方法
计数排序
双指针
日期
题目地址：https://leetcode.com/problems/sort-colors/description/

题目描述
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:

You are not suppose to use the library’s sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
1
2
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0’s, 1’s, and 2’s, then overwrite array with total number of 0’s, then 1’s and followed by 2’s.

Could you come up with an one-pass algorithm using only constant space?

题目大意
对乱序的0,1,2三个数字进行排序，保证结果是相同元素聚在一起。

解题方法
计数排序
因为只有三个数，所以简单的方法是计数排序。第一次遍历，统计出这三个数字出现的次数，第二次遍历，根据三个数字的次数对原列表进行修改。
"""
Runtime: 68 ms, faster than 6.70% of Python3 online submissions for Sort Colors.
Memory Usage: 13.7 MB, less than 86.51% of Python3 online submissions for Sort Colors.
"""
from collections import Counter
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        for i in xrange(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2

双指针
我看到这个题的时候，很明显的看出是要把一个数组分成三段，分别是小于v，等于v和大于v。由于只有三个数字，所以也就是0,1,2分别聚在一起。所以，这个题的考点来自快排之三项切分快速排序。在《算法》第四版中有介绍，也可以看快速排序及三向切分快速排序。

下面是题目讲解：

如果只能扫一遍，很容易想到的就是左边存放0和1，右边存放2.两边往中间靠。

设置两个指针，zero和two；zero指向第一个1的位置（0串的末尾），two指向第一个非2的位置。然后用i对nums进行遍历：

然后使用i从头到尾扫一遍，直到与two相遇。

i遇到0就换到左边去，遇到2就换到右边去，遇到1就跳过。

需要注意的是：由于zero记录第一个1的位置，因此A[zero]与A[i]交换后，A[zero]为0,A[i]为1，因此i++，zero++；

而two记录第一个非2的位置，可能为0或1，因此A[two]与A[i]交换后，A[two]为2,A[i]为0或1，i不能前进，要后续判断。
"""
Runtime: 32 ms, faster than 69.74% of Python3 online submissions for Sort Colors.
Memory Usage: 14 MB, less than 16.26% of Python3 online submissions for Sort Colors.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1


日期
2018 年 2 月 27 日
2019 年 1 月 5 日 —— 美好的周末又开始了
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://fuxuemingzhu.blog.csdn.net/article/details/79392195
