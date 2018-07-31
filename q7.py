class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n

    def __repr__(self):
        return str(self.value) + ' -> ' + str(self.next)

def reverseLinkedList(current):
    prev = None
    next = None
    while (current != None):
        next = current.next
        current.next = prev
        prev = current
        #prev.next = current
        current = next
    return prev


array = [1,2,3,8,9,5,6,4,7]

head = None
last = None
for a in array:
    cur = Node(a, None)
    if not head:
        head = cur
    else:
        last.next = cur
    last = cur

print(head)
head = reverseLinkedList(head)
print(head)


