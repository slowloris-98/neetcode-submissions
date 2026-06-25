class LinkedNode:
    def __init__(self, key, value):
        self.val = value
        self.next=None
        self.key = key
    
class LinkedList:
    def __init__(self):
        self.head=LinkedNode()

    def insertLL(self, key, value):
        new_node = LinkedNode(key,value)



class MyHashMap:

    def __init__(self):
        self.MOD = 10**6
        self.hm = [-1]*10**6
        

    def put(self, key: int, value: int) -> None:
        self.hm[key%self.MOD] = value

    def get(self, key: int) -> int:
        return self.hm[key%self.MOD]

    def remove(self, key: int) -> None:
        self.hm[key%self.MOD] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)