class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        total_length = length1 + length2 - 2
        middle = int(total_length / 2)
        i = 0
        j = 0
        mid_list = []
        mid = 0

        if (length1 == 0 or length2 == 0):

            try:
                if (length1 % 2 == 0):
                    return ((nums1[int(length1 / 2) - 1] + nums1[int(length1 / 2)]) / 2)
                else:
                    return (nums1[int(length1 / 2)])
            except:
                if (length2 % 2 == 0):
                    return ((nums2[int(length2 / 2 - 1)] + nums2[int(length2 / 2)]) / 2)
                else:
                    return (nums2[int(length2 / 2)])

        for k in range(middle + 2):

            if i < length1 and j < length2:

                if nums1[i] < nums2[j]:
                    mid = nums1[i]
                    i += 1

                else:
                    mid = nums2[j]
                    j += 1

            elif i >= (length1):

                remaining_position = middle + 1 - k
                if (len(mid_list) == 0):
                    mid_list.append(nums2[remaining_position + j - 1])
                    mid_list.append(nums2[remaining_position + j])
                elif (len(mid_list) == 1):
                    mid_list.append(nums2[remaining_position + j])


            elif (j >= length2):

                remaining_position = middle + 1 - k
                if (len(mid_list) == 0):
                    mid_list.append(nums1[remaining_position + i - 1])
                    mid_list.append(nums1[remaining_position + i])
                elif (len(mid_list) == 1):
                    mid_list.append(nums1[remaining_position + i])

            if len(mid_list) == 2:
                break

            if k == middle or k == middle + 1:
                mid_list.append(mid)

        if (length1 + length2) % 2 == 0:
            return sum(mid_list) / 2
        else:
            return mid_list[-1]


# [1, 3]
# [2]
first_number = []
second_number = [2, 3]
solution = Solution()
print(solution.findMedianSortedArrays(first_number, second_number))
