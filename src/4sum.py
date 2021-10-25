from typing import List


#

#
# class Solution:
#
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         res = []
#
#         for i in range(len(nums) - 3):
#             j = i + 1
#             k = j + 1
#             l = len(nums) - 1
#             remainder = target - nums[i]
#             while j <= len(nums) - 3:
#                 z = nums[i]
#                 a = nums[j]
#                 b = nums[k]
#                 c =  nums[l]
#                 if nums[k] + nums[l] + nums[j]  == remainder:
#                     res.append([nums[i], nums[j], nums[k], nums[l]])
#                     j += 1
#                     k = j + 1
#                     l = len(nums) - 1
#                 else:
#                     if k < l:
#                         if nums[k] + nums[l] + nums[j]  < remainder:
#                             l -= 1
#                         else:
#                             k = k + 1
#                     else:
#                         j += 1
#                         k = j + 1
#                         l = len(nums) - 1
#         return res
#
#
# print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
#
#
#
#
#

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)


ksum = Solution()
print(ksum.fourSum([1, 2, 3, 4, 4, 45, 6], 10))
