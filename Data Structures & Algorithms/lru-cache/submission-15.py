class Node:
    def __init__(self,key=None,val=None,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity         
        self.h = {} 
        self.head,self.tail = None,None

    def get(self, key: int) -> int:
        if key in self.h:
            node = self.h[key]
            #update ll if key not tail
            if node != self.tail:
                if node == self.head:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                if node.prev:
                    node.prev.next = node.next
                if self.tail:
                    self.tail.next = node
                else:
                    self.tail = node
                node.next = None
                node.prev = self.tail
                self.tail = self.tail.next  
            return self.h[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            node = self.h[key]
            node.val = value
            #update ll if key not tail
            if node != self.tail:
                if node == self.head:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                if node.prev:
                    node.prev.next = node.next
                if self.tail:
                    self.tail.next = node
                else:
                    self.tail = node
                node.next = None
                node.prev = self.tail
                self.tail = self.tail.next 
        else:
            if len(self.h)>=self.cap:
                #delete the LRU node
                del self.h[self.head.key]
                self.head = self.head.next
                if  self.head == None:
                    self.tail = None
                if self.head:
                    self.head.prev = None
            #add the newNode to MRU
            newNode = Node(key,value)
            if self.head == None:
                self.head = newNode
            if self.tail == None:
                self.tail = newNode
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = self.tail.next
            self.h[key] = newNode

        

