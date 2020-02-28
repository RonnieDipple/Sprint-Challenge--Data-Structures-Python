import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# value is the root of the tree
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # looks to see if there is a value
        if value < self.value:
            if self.left == None:
                # becomes the new value
                self.left = BinarySearchTree(value)
            else:
                # if there is a value then inserts it
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                # becomes the new value
                self.right = BinarySearchTree(value)
            else:
                # if there is a value then inserts it
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value:  # If something is in the tree, the helper method is_found is called
            # in is_find if the target is not in the tree the function returns None or True using recursion
            is_found = self._find(target, self)
            if is_found:
                return True
            else:
                return False

    def _find(self, target, current_node):
        if target > current_node.value and current_node.right:
            return self._find(target, current_node.right)
        elif target < current_node.value and current_node.left:
            return self._find(target, current_node.left)
        if target == current_node.value:
            return True

    # Return the maximum value found in the tree

    def get_max(self):
        current = self
        #While the is a number return the right most number which is the highest
        while(current.right is not None):
            current = current.right
        return current.value

        # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value == None:
            return

        #cb function in test
        cb(self.value)
        # Basically if left side is not null/none go left until it is, could put a print to watch it travel
        if self.left:
            self.left.for_each(cb)
        # Basically if right side is not null/none go right until it is, could put a print to watch it travel
        if self.right:
            self.right.for_each(cb)




    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        final = []

        def iop_helper(node):
            nonlocal final
            if node:
                iop_helper(node.left)

                final.append(node.value)

                iop_helper(node.right)

        iop_helper(node)
        for result in final:
            print(result)
        return final

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        stack = Queue()
        # root into stack
        stack.enqueue(node)
        #print(f"init stack len ={stack.len}")
        while stack.len != 0:
            temp: BinarySearchTree = stack.dequeue()
            if temp:
                if temp.right:
                    stack.enqueue(temp.right)
                if temp.left:
                    stack.enqueue(temp.left)
                print(temp.value)
            else:
                break

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        # root into stack
        stack.push(node)
        #print(f"init stack len ={stack.len}")
        while stack.len != 0:
            temp: BinarySearchTree = stack.pop()
            if temp:
                if temp.right:
                    stack.push(temp.right)
                if temp.left:
                    stack.push(temp.left)
                print(temp.value)
            else:
                break

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        final = []

        def preorder_helper(node):
            nonlocal final
            if node:
                final.append(node.value)

                preorder_helper(node.left)

                preorder_helper(node.right)

        preorder_helper(node)
        for result in final[0:]:
            print(result)
        return final

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        final = []

        def post_order_helper(node):
            nonlocal final
            if node:
                post_order_helper(node.left)

                post_order_helper(node.right)

                final.append(node.value)

        post_order_helper(node)
        for result in final[0:]:
            print(result)
        return final


class test():
    def try1(self):
        self.bst = BinarySearchTree(1)
        self.bst.insert(8)
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)
        # print(f"in order print return ="
        #       f"{self.bst.in_order_print(self.bst)}")
        # print(f"pre order print return ="
        #       f"{self.bst.pre_order_dft(self.bst)}")
        # print(f"post order print return ="
        #       f"{self.bst.post_order_dft(self.bst)}")
        print(f"^dft print^ ="
              f"{self.bst.dft_print(self.bst)}")


test = test()

test.try1()

# bst = BinarySearchTree()
# bst.insert(4)
# bst.insert(2)
# bst.insert(8)
# bst.insert(5)
# bst.insert(10)



#DFT Steps
# initialize a stack
# push root to stack
# while stack not empty
# pop top item of stack into temp
# do the thing
# if temp has right put in stack
# if temp has left put into stack
#

# BFT going wide aka doing each level at a time
# initialize a queue
# push root to queue
# while queue not empty
# pop top item of queue into temp
# do the thing
# if temp has right put in queue
# if temp has left put into queue
#
