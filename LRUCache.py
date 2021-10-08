class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node("head", -1), Node("tail", -1)
        self.head.right = self.tail
        self.tail.left = self.head
        self.cache = {}
  
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._accessKey(key)
        return self.cache[key].value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._accessKey(key)
            self.cache[key].value = value
        else:
            if len(self.cache) >= self.capacity:
                self._popLast()
            self.cache[key] = Node(key, value)
            self._addToLinkedList(self.cache[key])

    def _accessKey(self, key): # Retie it into the linked list
        if key in self.cache:
            self._removeFromLinkedList(self.cache[key])
        self._addToLinkedList(self.cache[key])
    
    def _popLast(self):
        node = self.head.right
        self._removeFromLinkedList(node)
        del self.cache[node.key]
        
    def _removeFromLinkedList(self, node): # Remove ties of node from linked list
        l, r = node.left, node.right
        l.right = r
        r.left = l

    def _addToLinkedList(self, node): # Tie node into linked list
        l, r = self.tail.left, self.tail
        l.right = node
        node.left = l
        r.left = node
        node.right = r

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)