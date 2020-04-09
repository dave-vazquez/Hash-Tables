import os

os.system('clear')


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return_str = ""
        current = self
        while current is not None:
            return_str += f"{{ key: {current.key}, value: {current.value} }} ->\n"
            current = current.next

        return return_str + "None"


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

        index = self._hash_mod(key)

        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)

        elif self.storage[index].key == key:
            self.storage[index].value = value

        else:
            prev = self.storage[index]
            current = self.storage[index].next

            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                else:
                    prev = current
                    current = current.next

            current = LinkedPair(key, value)
            prev.next = current

    def remove(self, key):

        index = self._hash_mod(key)

        if self.storage[index] is not None:

            if self.storage[index].key == key:
                self.storage[index] = self.storage[index].next
                self.entries -= 1

            else:
                prev = self.storage[index]
                current = self.storage[index].next

                while current is not None:
                    if current.key == key:
                        prev.next = current.next
                        self.entries -= 1
                        return
                    prev = prev.next
                    current = current.next

    def retrieve(self, key):
        index = self._hash_mod(key)

        current = self.storage[index]

        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next

        return current

    def resize(self):
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for linked_pair in old_storage:
            if linked_pair is not None:
                current = linked_pair
                while current is not None:
                    key = current.key
                    value = current.value
                    self.insert(key, value)
                    current = current.next

    def __str__(self):
        return_str = "[\n"

        for pair in self.storage:
            return_str += f"{pair},\n"

        return return_str + "]"


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
