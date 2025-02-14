class Solution:
    def isPalindrome(self, x: int) -> bool:
#convert to string to use indexing
        x = str(x)
#use step to check if it's the same reversed
        if x == x[::-1]:
            return True
        else:
            return False
        