class Solution:
    def romanToInt(self, s: str) -> int:
        key = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
        sum = 0 
        x = 0
        y = len(s)
        
        while x < y:
            if x < y - 1 and key[s[x]] < key[s[x + 1]]:
                sum += key[s[x + 1]] - key[s[x]]
                x += 2
            else: 
                sum += key[s[x]]
                x += 1
        return sum