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
    def remove(head,n):
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
    
    def insert(head,n,val):
        newNode = LinkedList(val)
        if (n==1):
            newNode.next = head
            return newNode
        curr = head
        for i in range(n-2):
            if curr is None:
                return head
            curr = curr.next
        if curr is None:
            return head
        newNode.next = curr.next
        curr.next = newNode
        return head
    
    def sort(head):
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left = LinkedList.sort(head)
        right = LinkedList.sort(mid)
        
        return LinkedList.merge(left,right)
    
    def merge(l1,l2):
        dummy = LinkedList()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1= l1.next 
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next 
        tail.next = l1 if l1 else l2
        return dummy.next
    
        
head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)

LinkedList.printList(head)

head = LinkedList.reverseLinkedList(head)
LinkedList.printList(head)

LinkedList.remove(head, 2)
LinkedList.printList(head)

LinkedList.insert(head, 2, 44)
LinkedList.printList(head)

head = LinkedList.sort(head)
LinkedList.printList(head)