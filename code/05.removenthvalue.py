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

    def removeNthValue(head,n):
        dummy = LinkedList(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for i in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

    def addToNthValue(head, n, val):
        new_node = LinkedList(val)
        if n == 1:
            new_node.next = head
            return new_node
        curr = head
        for i in range(n-2):
            if curr is None:
                return head  # Position out of bounds
            curr = curr.next
        if curr is None:
            return head  # Position out of bounds
        new_node.next = curr.next
        curr.next = new_node
        return head

head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)

LinkedList.printList(head)
head = LinkedList.removeNthValue(head,2)
LinkedList.printList(head)

head = LinkedList.addToNthValue(head, 3, 99)
LinkedList.printList(head)



# | Problem      | Technique            |
# | ------------ | -------------------- |
# | Middle node  | Fast & Slow          |
# | Remove nth   | Two pointers + dummy |
# | Reverse list | Prev, Curr, Next     |
# | Detect cycle | Fast & Slow          |
