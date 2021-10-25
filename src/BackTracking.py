# import itertools
#
# class Max_Chunks_To_Make_Sorted:
#     def init(self,s):
#         res = []
#         total = 1
#         self.back_traking(s,[],res)
#         return self.check(res,total)
#
#
#
#
#
#     def back_traking(self,s,path,res):
#         if not s:
#             res.append(path)
#             return
#         for i in range(1,len(s)+1):
#                 self.back_traking(s[i:],path+[s[:i]],res)
#
#     def check(self,res,total):
#
#         for v in res[1:]:
#             b = []
#             a = []
#             for j in v:
#                 if len(j) == 1:
#                     b.append(j[0])
#                 else:
#                     if(len(b) != 0):
#                         a = itertools.chain(a,sorted(b))
#                         b = []
#                     a = itertools.chain(a, sorted(j))
#             c = list(a)
#             print(c)
#             total = total + 1 if all(c[i] <= c[i + i] for i in range(len(c) - 2)) else total
#
#         return  total


# max_ =  Max_Chunks_To_Make_Sorted().init([2,1,3,4,4])
import collections
class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, (0, 0)
        for X, Y in zip(counted, sorted(counted)):
            print(type(cur))
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans


print(Solution().maxChunksToSorted([2, 1, 3, 4, 4]))
# print(max_)
#
# a = [[3], [1], [2]]
# b = [[3], [1], [2]], [[3], [1, 2]]
# c = [[3], [1], [2]], [[3], [1, 2]], [[3, 1], [2]]
# d = [[3], [1], [2]], [[3], [1, 2]], [[3, 1], [2]], [[3, 1, 2]]
# e = [[3], [1], [2]], [[3], [1, 2]], [[3, 1], [2]], [[3, 1, 2]]
#
#
# for i in e:
#     a = sorted(i)
#     print(a)
#     print(all(a[l] < a[l+1] for l in range(len(a)-2)))


#
# def len3(iterable):
#
#     """Calculate length by using enumerate and deque to iterate in C code
#     A trick borrowed from the cardinality library
#     O(n) in run time, but loop is in C
#     O(1) in memory"""
#
#     d = collections.deque(enumerate(iterable, 1), maxlen=1)
#     return d[0][0] if d else 0