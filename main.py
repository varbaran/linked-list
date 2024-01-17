class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# dummy -> 1 -> 2 -> 3 -> 4 -> 5
head = None
current = None
previous = None
for i in range(5):
    if head is None:
        head = LinkedList(i + 1)
        previous = head
        continue
    current = LinkedList(i + 1)
    previous.next = current
    previous = current

# current = head
# while current is not None:
#     print(current.value)
#     current = current.next
# for deleting
# current = head
# while current is not None:
#     if current.value == 3:
#         current.next = current.next.next
#     print(current.value)
#     current = current.next
# add value
current = head
while current is not None:
    if current.value == 3:
        new_node = LinkedList(10)
        new_node.next = current.next
        current.next = new_node
    print(current.value)
    current = current.next
# find value
current = head
while current is not None:
    if current.value == 3:
        print("found")
    print(current.value)
    current = current.next

