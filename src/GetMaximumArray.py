class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        maximum= 0
        num = {}
        for i in range(n+1):
            if i == 0:
                num[i] = 0
            elif i == 1:
                num[i] = 1
            elif i%2 == 0:
                num[i] = num[i/2]
            elif i%2 == 1:
                  num[i]=num[int(i/2)] + num[i+1]
            if maximum < num[i]:
                maximum = num[i]
        return maximum

print(Solution().getMaximumGenerated(5))