state = 0
inputarray = [
"6",
"1",
"2",
"2",
"3",
"3",
"4"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        lastdata = None
        while head:
            if (head.data != lastdata):
                print(head.data,end=' ')
            lastdata = head.data
            head = head.next




mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);