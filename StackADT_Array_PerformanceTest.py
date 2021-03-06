'''
Created on Mar 9, 2017

@author: Daniel McMahon
'''

from src.stack_ADT import stackADT
import time

def test_push():
        stack = stackADT()
        stack.stackPUSH([1,0])
        stack.stackPUSH([2,0])
        stack.stackPUSH([3,0])
        stack.stackPUSH([4,0])  
        stack.stackPUSH([5,0])
        stack.stackPUSH([0,0])
        stack.stackPUSH([0,1])
        stack.stackPUSH([0,2])
        stack.stackPUSH([0,3])
        stack.stackPUSH([0,4])
        stack.stackPUSH([0,5])

def test_pop():
        stack = stackADT()
        stack.stackPUSH([1,0])
        stack.stackPUSH([2,0])
        stack.stackPUSH([3,0])
        stack.stackPUSH([4,0])
        stack.stackPUSH([5,0])
        stack.stackPUSH([0,0])
        stack.stackPUSH([0,1])
        stack.stackPUSH([0,2])
        stack.stackPUSH([0,3])
        stack.stackPUSH([0,4])
        stack.stackPUSH([0,5])
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        
def test_count():
        stack = stackADT()
        stack.stackPUSH([1,0])
        stack.stackPUSH([2,0])
        stack.stackPUSH([3,0])
        stack.stackPUSH([4,0])
        stack.stackPUSH([5,0])
        stack.stackPUSH([0,0])
        stack.stackPUSH([0,1])
        stack.stackPUSH([0,2])
        stack.stackPUSH([0,3])
        stack.stackPUSH([0,4])
        stack.stackPUSH([0,5])
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()
        stack.pop()
        stack.size()


start1 = time.clock()
test_push()
print (time.clock() - start1, "seconds process time for Push test")

start2 = time.clock()
test_pop()
print (time.clock() - start2, "seconds process time for Pop test")

start3 = time.clock()
test_count()
print (time.clock() - start3, "seconds process time for Count test")
