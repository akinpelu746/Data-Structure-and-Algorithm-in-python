from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            j = i + 1
            k = j + 1
            l = len(nums) - 1
            remainder = target - nums[i]
            while j <= len(nums) - 3:
                z = nums[i]
                a = nums[j]
                b = nums[k]
                c = nums[l]
                if nums[k] + nums[l] + nums[j] == remainder:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    j += 1
                    k = j + 1
                    l = len(nums) - 1
                else:
                    if k < l:
                        if nums[k] + nums[l] + nums[j] < remainder:
                            l -= 1
                        else:
                            k = k + 1
                    else:
                        j += 1
                        k = j + 1
                        l = len(nums) - 1
        return res


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
