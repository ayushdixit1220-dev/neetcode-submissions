
from typing import List, Optional

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        current = self.head

        for _ in range(index):
            if current is None:
                return -1
            current = current.next

        if current is None:
            return -1

        return current.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if index < 0 or self.head is None:
            return False

        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        current = self.head

        for _ in range(index - 1):
            if current is None:
                return False
            current = current.next

        if current is None or current.next is None:
            return False

        removed_node = current.next
        current.next = removed_node.next

        if removed_node == self.tail:
            self.tail = current

        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        while current is not None:
            values.append(current.val)
            current = current.next

        return values
