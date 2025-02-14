# Brute Force Solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        chars = ""
        word = 1
        x, y = 0, 0
        while x < len(word1) and y < len(word2):
            if word == 1:
                chars += word1[x]
                x += 1
                word = 2
            else:
                chars += word2[y]
                y += 1
                word = 1
        while x < len(word1):
            chars += word1[x]
            x += 1
        
        while y < len(word2):
            chars += word2[y]
            y += 1  
        return chars
        # Let A be the length of Word1
        # Let B be the length of Word2
        # Let T = A + B
        
        # Time: O(T^2)
        # Space: O(T)


# Optimal Solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []

        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1
        
        while b < B:
            s.append(word2[b])
            b += 1
        
        return ''.join(s)
        # Let A be the length of Word1
        # Let B be the length of Word2
        # Let T = A + B
        
        # Time: O(T)
        # Space: O(T)