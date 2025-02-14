class Solution:
    def mySqrt(self, x: int) -> int:
        x = int(x)
        list = [1, 2, 3, 4]
        for y in list:
            if x % (y*y):
                return y
            else:
                return 69
    print(mySqrt(4))