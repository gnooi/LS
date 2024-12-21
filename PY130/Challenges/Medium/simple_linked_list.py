"""
- define a class Element
    - define an init method to accept 1 number
        - initialize self._datum to number
        - initializr self._next to None

    - define a property datum
        - return self._datum

    - define an instance method is_tail
        - if the element doesn't have a next, return True
        - otherwise, return False

    - define a property next
        - return the next element

- define a class SimpleLinkedList
    - define an init method
        - initialize an empty list
        - initialize self._head to none

    - define a property head
        - return the first element in the list
        - if the list is empty, return an appropriate value

    - define an instance method is_empty
        - return if length of list is 0

    - define an instance method push to accept 1 number
        - create an instance of element
        - append element to list
        - reassign self._head to last element pushed in list
    
    - define an instance method peek
        - pass

"""

class Element:
    def __init__(self, datum, next=None):
        self._datum = datum
        self._next = next

    @property
    def datum(self):
        return self._datum 
    
    @property
    def next(self):
        return self._next
    
    def is_tail(self):
        return self._next is None

class SimpleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def head(self):
        return self._head
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, datum):
        new_element = Element(datum, self.head)
        self._head = new_element
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        
        popped_element = self.head
        self._head = self.head.next
        self._size -= 1
        return popped_element.datum 
    
    def peek(self):
        return self.head.datum if self.head else None
    
    @classmethod
    def from_list(cls, data_list):
        new_list = cls()
        if data_list:
            for datum in reversed(data_list):
                new_list.push(datum)

        return new_list
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.datum)
            current = current.next

        return result 
    
    def reverse(self):
        reversed_list = SimpleLinkedList()
        current = self.head
        while current:
            reversed_list.push(current.datum)
            current = current.next

        return reversed_list
