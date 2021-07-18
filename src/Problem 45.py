# def jump(self, nums: int):
#     start = nums[0]
#     remaining_length = len(nums) - 2
#     steps = 1
#     if (len(nums) < 3):
#         return len(nums) - 1
#     elif (start > remaining_length):
#         return 1
#     while remaining_length >= 1:
#         if (steps == 1):
#
#             step = max(nums[0:start + 1])
#             step_index = nums[0:start + 1].index(step)
#             step_index = 1 if step_index == 0 else step_index
#             remaining_length -= step
#             steps += 1
#
#         else:
#             a = nums[step_index:nums[step] + 1]
#
#             step_index = 1 if step_index == 0 else step_index
#             steps += 1
#             remaining_length -= step
#     return steps


# solution = Solution()
# print(solution.jump([1, 1, 2, 1, 1]))


class Solution:
    def __init__(self, count=0):
        self.count = count

    def call(self, A):

        if (len(A) < 3):
            self.count += len(A) - 1
            return self.count
        self.jump(A)
        return self.count

    def Max_index(self, A, d):
        c = A[::-1]
        b = c.index(d)
        Maxindex = len(A) - b
        return Maxindex

    def jump(self, A):
        step = A[0]
        if len(A) == 1 or not A:
            return self.count
        elif step >= len(A) - 1:
            self.count += 1
            return self.count

        c = max(A[1:step + 1])
        if (c in A[2:step + 1]):
            step_index = self.Max_index(A[1:step + 1], c)
        else:
            step_index = A[1:step + 1].index(c)
        step_index = 1 if step_index == 0 else step_index
        self.count += 1
        self.jump(A[step_index:])


# A =  [2,3,1,1,2,3,4,4]
##print(solution.call([10,9,8,7,6,5,4,3,2,1,1,0]))
# [10,9,8,7,6,5,4,3,2,1,1,0]
# [1,1,2,1,1,1]
# [2,3,1,1,4])
# [1,3,2]
# [3,1,1,1,1]
# [1,2,3]
# 10,9,8,7,6,5,4,3,2,1,0

# def jump(nums):
#     if len(nums) <= 1: return 0
#     l, r = 0, nums[0]
#     times = 1
#     while r < len(nums) - 1:
#         times += 1
#         nxt = max(i + nums[i]  for i in range(l, r + 1))
#         l, r = r, nxt
#     return times
#
#
# print(jump([10,9,8,7,6,5,4,3,2,1,1,0]))


def possible(nums):
    if len(nums) <= 1: return True
    l, r = 0, nums[0]
    nxt = []
    while r < len(nums) - 1:
        for i in range(l, r + 1):
            nxt.append(i + nums[i])
        nxt.sort()
        while (len(nxt) > 0 and nums[nxt[-1]] == 0):
            nxt.pop()

        if (len(nxt)) <= 0: return False

        l, r = r, nxt[-1]
    return True


print(possible([1, 2, 3]))
