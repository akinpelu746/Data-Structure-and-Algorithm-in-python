class Solution:
    def fourSumCount(self, A, B, C, D):
        SumList = [A, B, C, D]
        self.lenght = len(A)
        self.count = 0
        first_list =
        self.SumCount(SumList, 0)

        return self.count

    def SumCount(self, SumList, total_sum):
        if (not SumList and total_sum == 0):
            self.count = self.count + 1
        elif (SumList):
            for i in range(self.lenght):
                self.SumCount(SumList[1:], total_sum + SumList[0][i])


(A,B,C,D) = ([1,2],[-2,-1],[-1,2],[0,2])
solution = Solution().fourSumCount(A,B,C,D)
print(solution)