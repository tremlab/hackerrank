# https://leetcode.com/problems/two-sum/description/

# refactored:

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        l = len(nums)

        for i in range(l):
            n = nums[i]
            match = target - n

            if str(match) in dict:
                return [dict[str(match)], i]

            dict[str(n)] = i


# ********************************
# this passes 26/29 tests
# 
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dict = {}
#
#         for i in range(len(nums)):
#             n = nums[i]
#             val = str(n)
#
#             if val in dict:
#                 dict[val].append(i)
#             else:
#                 dict[val] = [i]
#
#         print(dict)
#
#         for i in range(len(nums)):
#             n = nums[i]
#             val = str(target - n)
#
#             if val in dict:
#                 return [i, dict[val].pop()]
