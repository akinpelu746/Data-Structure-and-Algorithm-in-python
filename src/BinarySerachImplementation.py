"""Given a sorted array with duplicate elements. Find number of occurences of input key ."""


class BinaryImp:
    def __init__(self, array):
        self.array = array

    def low(self, l, r, key):
        while r - l > 1:
            m = int((l + (r)) / 2)
            if self.array[m] <= key:
                l = m
            else:
                r = m
        return l

    def high(self, l, r, key):
        while r - l > 1:
            m = int((l + r) / 2)
            if self.array[m] >= key:
                r = m
            else:
                l = m
        return r


list_input = [0, 0, 0, 0, 1, 2, 2, 2, 9, 8, 7]
binary = BinaryImp(list_input)
num_of_ocurrence = binary.low(0,9,2) - binary.high(0,9,2)+1
print( num_of_ocurrence)
