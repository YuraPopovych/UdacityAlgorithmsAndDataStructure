"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        POSITION_ITERATE = position - 1
        elementByPosition = self.head

        if position > 1:
            for i in range(POSITION_ITERATE):
                elementByPosition = elementByPosition.next
            return elementByPosition
        else:
            return elementByPosition

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        #Add new_element to link list
        le = LinkedList(new_element)

        numbers_of_iteration = range(1, position - 1)

        if position == 1:
            self.head = new_element
        elif(position == 2):
            self.head.next = new_element
        else:
            for i in numbers_of_iteration:
                iterator_element = self.head.next



        #TODO new element add to desire position
        #Unknow how to add to position which I want
        #What I have to do this? I have "next method"
        #Condition? iterate in loop for wanted amount of time
        #I have several condtion
        #TODO If position == 1
        #TODO if position > 1





        # elementByPosition = self.head
        #
        # #
        # POSITION_ITERATE = position - 2
        #
        # # 4rd element or greater
        # if POSITION_ITERATE > 1:
        #     for i in range(POSITION_ITERATE):
        #         elementByPosition = elementByPosition.next
        #     self.head = elementByPosition
        #     self.head.next = new_element
        # # 3rd element
        # elif(POSITION_ITERATE == 1):
        #     self.head.next = new_element





    def delete(self, value):
        """Delete the first node with a given value."""
        pass


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position !!!Get element by position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 1)

#ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(1).value)

# Test delete
#ll.delete(1)
# Should print 2 now
#print(ll.get_position(1).value)
# Should print 4 now
#print(ll.get_position(2).value)
# Should print 3 now
#print(ll.get_position(3).value)