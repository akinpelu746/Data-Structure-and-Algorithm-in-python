import numpy as np


class what_i_need:
    def __init__(self, s, current_value):
        self.total = 0
        self.total_num(s, current_value, 3)
        self.dp = {}

    def total_num(self, s, current_value, count):

        if count == 0:
            print(current_value)

            if 0 not in current_value:
                self.total += 1

            return
        for i in range(1, len(s) + 1):
            current_value = [x + y for x, y in zip(current_value, s[i - 1])]
            self.total_num(s[i:], current_value, count - 1)
            current_value = [x - y for x, y in zip(current_value, s[i - 1])]


d = np.zeros((5, 5))
s = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
what = what_i_need(s, [0, 0, 0, 0])

print(what)
