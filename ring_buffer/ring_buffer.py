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
        self.current = 0
        self.storage = DoublyLinkedList()


    def append(self, item):
        # Basically if nothing is in the ring
        # do this
        if self.current <= (self.capacity - 1):
            self.storage.add_to_tail(item) #Adds to the end
            self.current +=1 #moves current forward
        else:
            #basically if current has a value of say 2 use modulo operation to find
            # the correct area to add things in, in a chain
            mo = self.current % self.capacity
            head_to_be_updated = self.storage.head #head to be updated
            #chain loop using the modulo equation, this whole section
            # lays the items in the circular chain
            for i in range(mo):
                head_to_be_updated = head_to_be_updated.next
            head_to_be_updated.value = item
            self.current += 1


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head
        # While node is not none, append the node value to list buffer contents
        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

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
