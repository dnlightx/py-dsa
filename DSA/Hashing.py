# Hash sets
s = set()
print(s)

# Adding items to sets -> O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

# Lookup -> O(1)
if 1 in s:
    print("true")

# removing elements -> O(1)
s.remove(3) 
print(s)

# Set construction - O(S), S is the length of the string
# if you need to know the characters in a string when there are duplicates and don't need the amount of duplicates
string = "Heelloooh"
sett = set(string)
print(sett)

# Looping through the set -> O(N)
for x in s:
    print(x)
    
    
# HashMaps / Dictionaries
d = {"greg": 1, "steve": 2, "rob": 3}
print(d)

# adding a new key -> O(1)
d["promise"] = 4
print(d)

# looking up / checking for prescense -> O(1)
if "promise" in d:
    print("true")
    
# check the value of a key -> O(1)
print(d["greg"])

# Looping through the key:val pairs in a dict -> O(N)
for key, val in d.items(): 
    print(f"Key {key} : Value {val}")
    


# CHEATING LOL

#Default Dictionaries
from collections import defaultdict
default = defaultdict(list)
default[2]
print(default)

#Counter
from collections import Counter
string = "aaaaabbbbbcccdd"
counter = Counter(string)
print(counter)