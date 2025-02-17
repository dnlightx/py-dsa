# Strings
# Append to end of string - O(N)
s = "hello"
b = s + "z"
print(b)

# checking if in the string - O(N)
if "e" in s:
    print("True")



# Arrays
A = [1, 2, 3]
print(A)

#Appending at the end - O(1)
A.append(4)
print(A)

#Popping at the end(deleting) - O(1)
A.pop()
print(A)

# Inserting (not at the end) - O(N)
A.insert(2, 76)
print(A)

# Modifying an Element - 0(1)
A[0] = 12
print(A)    

# Acessing an element - O(1)
print(A[2])

# Accesing the last element - O(1)
print(A[-1])

if 12 in A:
    print("True")
    