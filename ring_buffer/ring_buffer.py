from doubly_linked_list import DoublyLinkedList
# Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get.
# The append method adds elements to the buffer.
# The get method, which is provided, returns all of the elements in the buffer in a list in their given order.
# It should not return any None values in the list even if they are present in the ring buffer.
#
# You may not use a Python List in your implementation of the append method (except for the stretch goal)
#
# Stretch Goal: Another method of implementing a ring buffer uses an array (Python List) instead of a linked list.
#     What are the advantages and disadvantages of using this method?
# What disadvantage normally found in arrays is overcome with this arrangement?


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.count = 0

    def append(self, item):
        count = self.count
        capacity = self.capacity
        if (count < capacity):
            self.storage[self.count] = item
            self.count += 1
        else:
            self.storage[0] =item
            self.count = 0
        return self.count

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
