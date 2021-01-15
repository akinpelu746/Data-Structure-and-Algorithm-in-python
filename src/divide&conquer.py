import math
def FindMaximumSubArray(low,mid,high,A =[]):
    sum_left = -math.inf
    sum=0
    max_left = 0
    for i in reversed(range(mid+1)):
        sum = sum+A[i]
        if sum > max_left:
            sum_left = sum
            max_left = i
    sum_right = -math.inf
    sum = 0
    max_right = 0
    for j in range(mid+1,high+1):
        sum = sum + A[j]
        if sum > sum_right:
            sum_right = sum
            max_right = j
    return (max_left,max_right,sum_left+sum_right)

def FindMaximumArray(low,high,A=[]):
    if low == high:
       return (low,high,A[low])
    else:
        mid = int((low + high)/2)
        (left_low,left_high,left_sum)  = FindMaximumArray(low,mid,A)
        (right_low,right_high,right_sum) = FindMaximumArray(mid+1,high,A)
        (cross_low,cross_high,cross_sum) = FindMaximumSubArray(low,mid,high,A)

    if left_sum > right_sum and left_sum> cross_sum:
        return (left_low,left_high,left_sum)
    else:
        if(right_sum>left_sum and right_sum>cross_sum):
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)
print(FindMaximumArray(low =0,high=15,A= [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]))

