class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def print_list(head):
    while head != None:
        print(head.data)
        head = head.next

def Insert(head, data):
    node = Node(data, None)
    if not head:
        return node
    else:
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = node
    return head

head = Insert(None, data=4)
head = Insert(head, data=2)
head = Insert(head, data=3)
head = Insert(head, data=4)
head = Insert(head, data=1)



print_list(head)