"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    #Pointers
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev


    """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    # Pointers, this is not mandatory but they are useful
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    # Basically the lower level/ Guts version of len(my_array)
    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    # Dependency chain
    # Planning
    # What do we need to think about?
    # What are the scenarios?
    # This needs to be head because we're adding to head
    # Update previous head
    # Update length
    # Edge cases? -- If self.head is none then there is no list and no tail
    # If there is no tail...New head becomes new tail as well
    #Step 1
    def add_to_head(self, value):
        #The create a linked list we need to:
        # Create a node
        # new_node = ListNode (value)
        # Add to the length although that is not dependent on anything
        self.length += 1
        #
        if not self.head and not self.tail:
            #If you have an empty list, this is what you do, self aka this head and tail
            self.head = new_node = self.tail = ListNode(value)
        else:

            # If head and tail are not empty we know the list is populated
            # Need to do this is a way that we don't lose anything
            # need to update new nodes.head because we are about to move that and lose where it is
            # new_node.next = self.head
            # self.head.prev = new_node
            self.head.insert_before(value)
            # self.head = new_node
            self.head = self.head.prev






    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    #Step 2 almost identical to step 1 add_to_head
    def add_to_tail(self, value):
        # Add to the tail
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node = self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #Uses already written code
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        # Not getting a null pointer in add_to_tail even though it is referencing a supposedly deleted node because
        # node still exists we are just moving pointers here and
        # garbage collection will probably get rid of it in the future
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    # Step 3 is similar to steps 1and 2 and we can reuse delete in remove
    # doing this allows us to handle edge cases

    def delete(self, node):
        # What do we need to keep track of?
        # The length because deleting something from a linked list changes the length as it would in any list
        # planning
        # If linked list is empty
        if not self.head and not self.tail:
            print("Error: Attempted to delete node not in list")
            return
        # If node is both
        elif self.head == self.tail:
        # no need to delete the node as garbage collection will take care of it
            self.head = None
            self.tail = None
        # If node is head
        # If node is both
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        # If node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()

        # If node is in middle
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        # Plan
        # Make var
        # Loop through nodes via node.next aka go to every node
        # Update var to highest, If node.value is higher, update max
        # return var, return max

        current = self.head
        #Edge case
        if(self.head == None):
            print("List is empty")
            return 0
        else:
            max = self.head.value

            #The loop
            while(current!= None):
                #If current value is above max aka self head move on otherwise max = current value
                if(current.value > max):
                    max = current.value
                current = current.next
        return max




