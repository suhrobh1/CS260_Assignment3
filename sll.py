# Name: Suhrob Hasanov
# OSU Email: hasanovs@oregon
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 2/13/23
# Description: Singly Linked List implementation

from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:

    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Inserts value to the front of the linked list.
        """

        node = SLNode(value)
        # New node now points to what head was pointing to
        node.next = self._head.next
        self._head.next = node

    def insert_back(self, value: object) -> None:
        """
        Inserts value to be back of the linked list.
        """
        # print("self.head value: ", self._head.value)
        if self._head.value is None:
            self._head = SLNode(value)
            self.insert_front(value)

        else:
            current_node = self._head
            # Setting up loop count
            while_range = self.length()
            # Getting to the end of the linked list and "adding the node"
            while(while_range >= 0):
                if(current_node.next is None):
                    current_node.next = SLNode(value)
                current_node = current_node.next
                while_range -= 1


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert the given node at the given index.
        """
        current_node = self._head
        if index < 0 or index > self.length():
            raise SLLException

        # Iterating over to the given index
        for i in range(0, index + 1):
            # If we at the index, we add the new node
            if index == i:
                temp = current_node.next
                new_node = SLNode(value)
                current_node.next = new_node
                new_node.next = temp
            current_node = current_node.next


    def remove_at_index(self, index: int) -> None:
        """
        Removes node at the given index.
        """
        previous_node = self._head
        current_node = self._head.next

        if index < 0 or index > self.length() - 1:
            raise SLLException

        # Iterating over to the node at index and removing pointer to it "removing it"
        for i in range(0, index):
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next

        return


    def remove(self, value: object) -> bool:
        """
        Removes node with given value.
        """
        current_node = self._head.next
        # Iterating and looking for the node with given value
        for i in range(self.length()):
            if(current_node.value == value):
                # If found, we call remove function and return True
                self.remove_at_index(i)
                return True
            current_node = current_node.next
        # If not found returning False
        return False

    def count(self, value: object) -> int:
        """
        Counts occurence of the node with given node.
        """
        current_node = self._head.next
        count = 0
        # Looking for the value and adding to count if it's there
        for i in range(self.length()):
            if (current_node.value == value):
                count += 1
            current_node = current_node.next
        return count

    def find(self, value: object) -> bool:
        """
        Returns boolean value depending whether value is present.
        """
        current_node = self._head.next
        for i in range(self.length()):
            if (current_node.value == value):
                return True
            current_node = current_node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Returns section of the list from given index and given size.
        """
        if (start_index < 0 or start_index > self.length() - 1):
            raise SLLException
        if (size > self.length() - start_index or size < 0):
            raise SLLException


        newList = LinkedList()
        current_node = self._head
        # If the size requested zero
        if size == 0:
            return newList
        # If requested size is one
        if size == 1:
            for i in range(0, self.length()):
                # If the index needed matches the iterated index
                if (i == start_index):
                    current_node= current_node.next
                    newList.insert_front(current_node.value)
                    return newList
                current_node = current_node.next

        # In this block we establish the node that will be the starting node for slicing
        starting_node = None
        for i in range(0, self.length()):
            if (i == start_index):
                # print("node value", current_node.value)
                starting_node = current_node.next
                break
            current_node = current_node.next

        # Once we established the starting node, we loop to add it and remaining nodes
        for i in range(0, size):
            newList.insert_back(starting_node.value)
            starting_node = starting_node.next

        return newList

if __name__ == "__main__":

    # print("\n# insert_front example 1")
    # test_case = ["A", "B", "C"]
    # lst = LinkedList()
    # for case in test_case:
    #     lst.insert_front(case)
    #     print(lst)

    # print("\n# insert_back example 1")
    # test_case = ["C", "B", "A"]
    # lst = LinkedList()
    # for case in test_case:
    #     lst.insert_back(case)
    #     print(lst)

    # print("\n# insert_at_index example 1")
    # lst = LinkedList()
    # test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    # for index, value in test_cases:
    #     print("Inserted", value, "at index", index, ": ", end="")
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print("\n# remove_at_index example 1")
    # lst = LinkedList([1, 2, 3, 4, 5, 6])
    # print(f"Initial LinkedList : {lst}")
    # for index in [0, 2, 0, 2, 2, -2]:
    #     print("Removed at index", index, ": ", end="")
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))

    # print("\n# remove example 1")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [7, 3, 3, 3, 3]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    # print("\n# remove example 2")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))









    print("_----------------------------------------------------------------------")

    lst = LinkedList([-69911 , 7754 , 14546,-37436 , 85109,-24272, 5464])
    ll_slice = lst.slice(0, 6)
    print("Source:", lst)
    print("Start: 0 Size: 6 :", ll_slice)
    # ll_slice.remove_at_index(0)
    # print("Removed at index 0 :", ll_slice)

    lst = LinkedList([-39758 , -38721 ,57359])
    ll_slice = lst.slice(1, 1)
    print("Source:", lst)
    print("Start: 1 Size: 1 :", ll_slice)
    # ll_slice.remove_at_index(0)
    # print("Removed at index 0 :", ll_slice)
    print("_----------------------------------------------------------------------")

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(6, 1), (0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
