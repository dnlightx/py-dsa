class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels="aeiou"
        x=[]
        for i in words:
            if i[0] in vowels and i[-1] in vowels:
                x.append(1)
            else:
                x.append(0)
                
        y=[0]*(len(x)+1)
        
        for i in range(len(x)):
            y[i+1]=y[i]+x[i]
        output=[]
        
        for l,r in queries:
            output.append(y[r+1]-y[l])
        return output