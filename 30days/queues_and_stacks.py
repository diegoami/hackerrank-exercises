#!/bin/python


inputarray = [
"racecara"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

from collections import deque
class Solution:

    stack = deque()
    queue = deque()

    def pushCharacter(self, obj):
        self.stack.append(obj)

    def enqueueCharacter(self, obj):
       self.queue.append(obj)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()

s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
