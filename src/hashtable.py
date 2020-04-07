import os

os.system('clear')


class Error(Exception):
    pass


class CollisionError(Error):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"ColissionError, {self.message}"
        else:
            return "CollisionError has been raised"


class KeyNotFoundError(Error):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"KeyNotFoundError, {self.message}"
        else:
            return "KeyNotFoundError has been raised"
# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.entries = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):

        index = self._hash_mod(key)

        # if there's nothing stored at the hashed index
        if self.storage[index] is None:
            # start a new linked list with the key value pair
            self.storage[index] = LinkedPair(key, value)

        # else if the head of the linked list matches the key
        elif self.storage[index].key = key:
            # overwrite the value
            self.storage[index].value = value

        # else begin the traversal
        else:
            # make 'current' the head's 'next' of the linked list
            inserted = False
            current = self.storage[index].next

            # traverse
            while current.next is not None and inserted is False:
                # and overwrite the value if the key exists
                if current.key == key:
                    current.value = value
                    inserted = True

            # if no insertion took place and we're at the end of the linked list
            if not inserted:
                # make current.next the new entry
                current.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # SOLUTION:
        index = self._hash_mod(key)

        if self.storage[index] is None:
            raise KeyNotFoundError(f"Key {key} was not found in the table.")
        else:
            value = self.storage[index][1]
            self.storage[index] = None

            return value

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # SOLUTION:
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None

        return self.storage[index][1]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        self.capacity *= 2

        new_storage = [None] * self.capacity

        for pair in self.storage:
            if pair is not None:
                key = pair[0]
                value = pair[1]
                index = self._hash_mod(key)
                new_storage[index] = (key, value)

        self.storage = new_storage


ht = HashTable(3)

ht.insert("key-0", "val-0")
print("inserted key-0, val-0")
ht.insert("key-1", "val-1")
print("inserted key-1, val-1")
ht.insert("key-2", "val-2")
print("inserted key-2, val-2")

# print("retrieving key-0:")
# print(ht.retrieve("key-0"))
# print("")
# print("retrieving key-1:")
# print(ht.retrieve("key-1"))
# print("")
# print("retrieving key-2:")
# print(ht.retrieve("key-2"))
# print("")

# print("removing key-2:")
# print(ht.remove("key-2"))
# print("")

# print("resulting storage:")
# print(ht.storage)
# print("")

# print("resizing storage:")
# ht.resize()
# print(ht.storage)

# print(ht.remove("key-0"))

# ht.insert("key-8", "val-8")
# ht.insert("key-9", "val-9")


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
