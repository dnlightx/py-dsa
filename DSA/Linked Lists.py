#Singly Linked Lists

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(4)

Head.next = A
A.next = B
B.next = C

print(f"Op1: {Head}")

# Traversing the list -> O(n)
curr = Head
while curr:
#this while loop is basically saying that while the value of curr is valid and not a null/none value keep printing the next node
    print(f"Op2: {curr}")
    curr = curr.next

# Displaying the list -> O(n)
def display(Head): 
    curr = Head
    list = []
    while curr:
        list.append(str(curr))
        curr = curr.next
#join method is = used to join the elements of the list with a certain character of your choice
    f = " -> ".join(list)
    print(f"Op3: {f}")

display(Head)   

# Searching for a node
def search(Head, val):
    curr = Head
    while curr:
        if curr.val == val:
            return True
        curr = curr.next    
    return False
           
print(bool(search(Head, 3)))

#Doubly Linked Lists
class DoublyNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)

Head = DoublyNode(1)
A = DoublyNode(3)
B = DoublyNode(5)
C = DoublyNode(4)

Head.next = A
A.prev = Head
A.next = B
B.prev = A
B.next = C
C.prev = B

# Disply nodes - O(n)
def display(Head):
    curr = Head
    list = []
    while curr:
        list.append(str(curr))
        curr = curr.next
    print(" <-> " .join(list))

display(Head)

