class LinkedNode:
    def __init__(self, key, value):
        self.val = value
        self.next=None
        self.key = key
    
class LinkedList:
    def __init__(self):
        self.head=LinkedNode(-1,-1)

    def insertNode(self, key, value):
        new_node = LinkedNode(key,value)
        curr=self.head.next
        prev=self.head
        while curr:
            if curr.key==key:
                curr.val=value
                return
            prev=curr
            curr=curr.next
        prev.next=new_node
    
    def removeNode(self, key):
        curr=self.head.next
        prev=self.head

        if not curr:
            self.head=LinkedNode(-1,-1)

        while curr:
            if curr.key == key:
                prev.next=curr.next
                break
            prev=curr
            curr=curr.next
    
    def getNode(self, key):
        curr=self.head.next
        while curr:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1
            
class MyHashMap:

    def __init__(self):
        self.MOD = 10**3
        self.hm = [LinkedList()]*self.MOD

    def put(self, key: int, value: int) -> None:
        self.hm[key%self.MOD].insertNode(key, value)

    def get(self, key: int) -> int:
        return self.hm[key%self.MOD].getNode(key)

    def remove(self, key: int) -> None:
        self.hm[key%self.MOD].removeNode(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)