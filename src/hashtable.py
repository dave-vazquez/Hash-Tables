import os

os.system('clear')


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{{ key: {self.key}, value: {self.value} }}"


class HashTable:

    def __init__(self, capacity):
        self.entries = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):

        return hash(key)

    def _hash_djb2(self, key):
        # TODO
        pass

    def _hash_mod(self, key):

        return self._hash(key) % self.capacity

    def insert(self, key, value):

        #TODO try again.
      
    def remove(self, key):

        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None

        else:
            current = self.storage[index]
            prev = None

            while current is not None:
                if current.key == key:
                    value = current.value
                    current = None
                    prev.next = current.next
                    self.entries -= 1
                    return value
                prev = current
                current = current.next

            return None

    def retrieve(self, key):
        index = self._hash_mod(key)
        # store the value of the hashed index in current
        current = self.storage[index]

        # if the value is None, this loop won't run at all
        # and instead will skip right to the return, returning None
        # if the value is NOT none, the loop starts until it finds the 
        # key, returns the value, or loops all the way to the end of 
        # the list, None, and returns None as the value
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next

        return current

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        self.capacity *= 2

        new_storage = [None] * self.capacity

        for linked_pair in self.storage:
            if linked_pair is not None:
                key = linked_pair.key
                value = linked_pair.value
                index = self._hash_mod(key)
                new_storage[index] = LinkedPair(key, value)

        self.storage = new_storage


ht = HashTable(8)

ht.insert("key-0", "val-0")
# ht.insert("key-1", "val-1")
# ht.insert("key-2", "val-2")
# ht.insert("key-3", "val-3")
# ht.insert("key-4", "val-4")
# ht.insert("key-5", "val-5")
# ht.insert("key-6", "val-6")
# ht.insert("key-7", "val-7")
# ht.insert("key-8", "val-8")
# ht.insert("key-9", "val-9")

print(ht.storage)


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
