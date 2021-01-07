class Node(object):

        def __init__(self, value):
                self.value = None
                self.next_node = None
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

def nth_to_last_node(n, head):
        left_pointer = head
        right_pointer = head
        
        for i in range(n - 1):
                if not right_pointer.next_node:
                        raise LookupError('Error: n is larger than the linked list')
                        
                right_pointer = right_pointer.next_node
                
        while right_pointer.next_node:
                left_pointer = left_pointer.next_node
                right_pointer = right_pointer.next_node
                
        return left_pointer
        
print(nth_to_last_node(2, a) == d)