class Node:
    # Node class to represent each element in the doubly linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # LRUCache class to handle operations of the cache
    def __init__(self, capacity: int):
        self.capacity = capacity  # store the maximum capacity of the cache
        self.cache = {}  # hash map to store the keys and their corresponding node references
        self.head = Node(0, 0)  # dummy head of the doubly linked list
        self.tail = Node(0, 0)  # dummy tail of the doubly linked list
        self.head.next = self.tail  # initialize doubly linked list
        self.tail.prev = self.head

    def _remove(self, node: Node):
        # private helper function to remove a node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        # private helper function to add a node right after the head
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        # get the value of the node with the given key
        node = self.cache.get(key)
        if not node:
            return -1  # if key doesn't exist, return -1
        self._remove(node)  # remove the node from its current position
        self._add(node)  # add the node right after the head (mark as recently used)
        return node.value

    def put(self, key: int, value: int):
        # insert or update the value of the key
        node = self.cache.get(key)
        if node:
            self._remove(node)  # if node exists, remove it first
        node = Node(key, value)  # create a new node
        self._add(node)  # add the node right after the head
        self.cache[key] = node  # store the reference in the hash map
        if len(self.cache) > self.capacity:
            # if cache size exceeds capacity, remove least recently used item
            lru_node = self.tail.prev
            self._remove(lru_node)  # remove the node from linked list
            del self.cache[lru_node.key]  # remove the node from hash map
