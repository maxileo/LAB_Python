# EX 1

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.previous = None

# class Stack:
#    def __init__(self):
#        self.top = None

#    def push(self, element):
#        new_node = Node(element)
#        new_node.previous = self.top
#        self.top = new_node
   
#    def peek(self):
#        if self.top == None:
#            return None
#        return self.top.value
   
#    def pop(self):
#        if self.top == None:
#            return None
#        element = self.top.value
#        self.top = self.top.previous
#        return element
   
# stack = Stack()
# stack.push(5)
# stack.push(7)
# stack.push(8)
# print(stack.peek())
# print(stack.pop())
# print(stack.pop())
# stack.push(9)
# print(stack.pop())
# print(stack.pop())

# EX 2

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Queue:
#    def __init__(self):
#        self.first = None

#    def push(self, element):
#        new_node = Node(element)
#        if self.first == None:
#            self.first = new_node
#        else:
#            element = self.first
#            while element.next != None:
#                element = element.next
#            element.next = new_node
           
#    def peek(self):
#        if self.first == None:
#            return None
#        return self.first.value
   
#    def pop(self):
#        if self.first == None:
#            return None
#        element = self.first.value
#        self.first = self.first.next
#        return element
   
# queue = Queue()
# queue.push(5)
# queue.push(7)
# queue.push(8)
# print(queue.peek())
# print(queue.pop())
# print(queue.pop())
# queue.push(9)
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())

# EX 3
#import copy
#
#class Matrix:
#    def __init__(self, n, m):
#        self.n = n
#        self.m = m
#        self.values = []
#        for i in range(self.n):
#            line = []
#            for j in range(self.m):
#                line.append(0)
#            self.values.append(line)
#    
#    def print(self):
#        for i in range(self.n):
#            for j in range(self.m):
#                print(self.values[i][j], end=" ")
#            print("")
#
#    def set(self, i, j, value):
#        if i >= 0 and i < self.n and j >= 0 and j < self.m:
#            self.values[i][j] = value
#            return True
#        else:
#            return False
#        
#    def get(self, i , j):
#        if i >= 0 and i < self.n and j >= 0 and j < self.m:
#            return self.values[i][j]
#        else:
#            return None
#        
#    def transform(self, callback_func):
#        for i in range(self.n):
#            for j in range(self.m):
#                self.values[i][j] = callback_func(self.values[i][j])
#
#    def transpose(self):
#        newMatrix = Matrix(self.m, self.n)
#        for i in range(self.n):
#            for j in range(self.m):
#                newMatrix.set(j, i, self.values[i][j])
#        self.n = newMatrix.n
#        self.m = newMatrix.m
#        self.values = copy.deepcopy(newMatrix.values)
#
#    def multiply(self, matrixB):
#        if matrixB.n != self.m:
#            return False
#        resultMatrix = Matrix(self.n, matrixB.m)
#        for i in range(self.n):
#            for j in range(matrixB.m):
#                newValue = 0
#                for k in range(self.m):
#                    newValue = newValue + self.values[i][k] * matrixB.get(k, j)
#                resultMatrix.set(i, j, newValue)
#        self.n = resultMatrix.n
#        self.m = resultMatrix.m
#        self.values = copy.deepcopy(resultMatrix.values)
#        return True
#
#
#
#a = Matrix(2, 3)
#a.set(0, 0, 1)
#a.set(0, 1, 2)
#a.set(0, 2, 3)
#a.set(1, 0, 4)
#a.set(1, 1, 5)
#a.set(1, 2, 6)
#b = Matrix(3, 2)
#b.set(0, 0, 10)
#b.set(0, 1, 11)
#b.set(1, 0, 20)
#b.set(1, 1, 21)
#b.set(2, 0, 30)
#b.set(2, 1, 31)
#a.multiply(b)
#a.print()
#
#c = Matrix(3, 4)
#c.set(1, 1, 5)
#c.set(1, 2, 6)
#c.transform(lambda x: x + 2)
#c.print()
#
#c.transpose()
#c.print()
