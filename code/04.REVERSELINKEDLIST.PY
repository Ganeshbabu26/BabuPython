# class LinkedList:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next

#     def reverseLinkedList(head):
#         # prev = None
#         # curr = head

#         # while curr:
#         #     nxt = curr.next
#         #     curr.next = prev
#         #     prev = curr
#         #     curr = nxt
#         # return prev
#         if head is None or head.next is None:
#             return head

#         newHead = LinkedList.reverseLinkedList(head.next)

#         head.next.next = head
#         head.next = None

#         return newHead

#     def printList(head):
#         curr = head
#         while curr:
#             print(curr.val,end=" -> ")
#             curr = curr.next
#         print(None)
# head = LinkedList(1)
# head.next = LinkedList(2)
# head.next.next = LinkedList(3)
# head.next.next.next = LinkedList(4)
# head.next.next.next.next = LinkedList(5)

# LinkedList.printList(head)
# head = LinkedList.reverseLinkedList(head)
# LinkedList.printList(head)








class LinkedList:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def reverseLinkedList(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def printList(head):
        curr = head
        while curr:
            print(curr.val,end=" -> ")
            curr = curr.next
        print(None)

head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)

h = LinkedList
print("-----Original LinkedList-----\n")

h.printList(head)
head = h.reverseLinkedList(head)
print("\n\n-----Reversed LinkedList-----\n")
h.printList(head)

# head = LinkedList(1)
# head.next = LinkedList(2)
# head.next.next = LinkedList(3)
# head.next.next.next = LinkedList(4)
# head.next.next.next.next = LinkedList(5)

# LinkedList.printList(head)
# head = LinkedList.reverseLinkedList(head)
# LinkedList.printList(head)

# | curr        | prev           | action               |
# | ----        | ----             | -------------       |
# | 1            | None           | 1.next = None    |
# | 2           | 1                 | 2.next = 1           |
# | 3           | 2                | 3.next = 2          |
