# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
        self.parent =  None

    def __str__(self):
        return f'value: {self.value}, right: {self.right}, left: {self.left}'


    def insert_node(self, value):
        if value >= self.value:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert_node(value)
        else:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert_node(value)

    def contains_node(self, value):
            
            if self.value == value:
                return True
            if value > self.value:
                if not self.right:
                    return False
                else:
                    self.right.contains_node(value)
            if value < self.value:
                if not self.left:
                    return False
                else:
                    self.left.contains_node(value)




class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

    def __str__(self):
        return f'Root: {self.root}'


    # Insert the given value into the tree
    def insert(self, value):
        if self.root:
            self.root.insert_node(value)
        else:
            self.root = Node(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if not self.root:
            return False
        else:
            self.root.contains_node(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self.root
        while True:
            current_node = current_node.right
            if not current_node.right:
                return current_node.value



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# b = BinarySearchTree(3)
# b.insert(4)
# b.insert(5)
# b.insert(1)
# print(b)