class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtStart(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAtEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node
        
    def printLinkedList(self):
        itr = self.head
        while itr:
            print(itr.data,end='-->')
            itr = itr.next
        print()
    
    def lengthOfLinkedList(self):
        if self.head is None:
            return "EMPTY"
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count = count+1
        return count
    
    def deleteAtStart(self):
        if self.head is None:
            return "EMPTY"
        self.head = self.head.next
    
    def deleteAtEnd(self):
        if self.head is None:
            return "EMPTY"
        
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None
    
    def insertAtIdx(self,idx,new_data):
        if idx<0 or idx>self.lengthOfLinkedList():
            return "Give proper index"
        
        if idx==0:
            self.insertAtStart(new_data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == idx-1:
                new_node = Node(new_data)
                new_node.next = itr.next
                itr.next = new_node
                break
            
            itr = itr.next
            count = count+1                
        
    
if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtStart("A")
    llist.insertAtStart("B")
    llist.insertAtEnd("0")
    llist.insertAtEnd("1")
    print("Length:",llist.lengthOfLinkedList())
    llist.printLinkedList()
    llist.deleteAtStart()
    print("Length:",llist.lengthOfLinkedList())
    llist.printLinkedList()
    llist.deleteAtEnd()
    print("Length:",llist.lengthOfLinkedList())
    llist.printLinkedList()
    llist.insertAtIdx(1,"1")
    print("Length:",llist.lengthOfLinkedList())
    llist.printLinkedList()
    llist.insertAtIdx(2,"2")
    print("Length:",llist.lengthOfLinkedList())
    llist.printLinkedList()
