import operator
from collections import deque

class TwentyFourSolver:

    ops = ['+', '-', '*', '/']

    def permuteUnique(self, arr):
        ret = [[]]
        for n in arr:
            ret = [l[i:]+[n]+l[:i]
                   for l in ret
                   for i in range((l+[n]).index(n)+1)]
        return ret

    def combination(self, k, arr):
        ret = [[]]
        if k == 0:
            return ret
        ret = [pre + [i] 
                for i in arr
                for pre in self.combination(k-1, arr[:-1])]
        return ret

    def merge(self, arr1, arr2):
        temp = [i
                for j, k in zip(arr1, arr2)
                for i in [j, k]]
        min_len = min(len(arr1), len(arr2))
        ret = temp + arr1[min_len:] + arr2[min_len:]
        return ret

    def linear_eval(self, arr):
        ops_map = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
        }

        ops = list()
        res = int(arr[0])
        for i in arr[1:]:
            try:
                i = int(i)
                op = ops.pop()
                res = ops_map[op](res, i)
            except:
                ops.append(i)
        return res

    def solve(self, nums):
        ops_com = self.combination(3, self.ops) 
        candidates = [self.merge(nums_perm, ops) 
                        for ops in ops_com
                        for nums_perm in self.permuteUnique(nums)]
        for candidate in candidates:
            res = self.linear_eval(candidate)
            if res == 24:
                print(candidate)
                return
        print("No solution")
        
if __name__ == '__main__':
    text = input("Please input the numbers separated by space:\n")
    nums = text.split()
    t = TwentyFourSolver()
    t.solve(nums)