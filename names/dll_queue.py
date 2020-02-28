import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queues, like the name suggests, follow the First-in-First-Out (FIFO) principle.
# As if waiting in a queue for the movie tickets,
# the first one to stand in line is the first one to buy a ticket and enjoy the movie.

class Queue:
    #Plan
    def __init__(self):
        self.size = 0
        # Why is our Doubly Linked List a good choice to store our elements?
        self.storage = DoublyLinkedList()
        self.head  = None
        self.last = None

    # enqueue() : Adds element to the back of Queue.
    # Need to add to tail
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        #Increase the size of the tail
        self.size += 1

    # dequeue() : Removes and returns the first element from the queue.
    def dequeue(self):
        # self.dictionary.remove_from_head(self.value) <- this is wrong no need to add the value only to take it away
        # as the value is already in head
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()





    # len returns the number of items in the queue.
    def len(self):
        return self.size
