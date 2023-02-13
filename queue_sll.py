# Name: Suhrob Hasanov
# OSU Email: hasanovs@oregon
# Course: CS261 - Data Structures
# Assignment: Assignment 3
# Due Date: 2/13/23
# Description: Queue ADT class implementation with singly linked list


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds the given value to the queue.
        """
        new_node = SLNode(value)

        # Is it empty?
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        # If not empty, the tail points to the new node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        """
        Removes the value from the queue from the front.
        """

        if self.is_empty():
            raise QueueException
        # If list not empty, the head will point to the node behind the front one
        else:
            temp = self._head
            self._head  = self._head.next
            return temp.value

    def front(self) -> object:
        """
        Returns the value at the front of the queue.
        """
        if self.is_empty():
            raise QueueException
        else:
            return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
