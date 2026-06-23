class ListNode:
    def __init__(self, value):
        self.val=value
        self.nxt=None
    
class LinkedList:
    def __init__(self):
        self.head=ListNode(None)
    
    def insertNode(self, node: ListNode):
        curr=self.head

        while curr and curr.nxt:
            curr=curr.nxt
        curr.nxt=node
    
    def removeNode(self, key):
        curr=self.head.nxt
        prev=self.head
        while curr:
            if curr.val==key:
                prev.nxt=curr.nxt
                return
            prev=curr
            curr=curr.nxt

    def checkNode(self, key):
        curr=self.head
        while curr:
            if curr.val==key:
                return True
            curr=curr.nxt
        return False
        

class MyHashSet:
    
    def __init__(self):
        self.LL=LinkedList()

    def add(self, key: int) -> None:
        if self.contains(key):
            self.remove(key)
        self.LL.insertNode(ListNode(key))

    def remove(self, key: int) -> None:
        self.LL.removeNode(key)

    def contains(self, key: int) -> bool:
        return self.LL.checkNode(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)