class MyHashSet:
    
    def __init__(self):
        self.MOD = 10**6    
        self.arr=[-1]*self.MOD

    def add(self, key: int) -> None:
        self.arr[key%self.MOD]=key

    def remove(self, key: int) -> None:
        self.arr[key%self.MOD]=-1

    def contains(self, key: int) -> bool:
        if self.arr[key%self.MOD]!=-1:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)