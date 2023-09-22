# 1D Array
arr_1d = [2,8,6]
el1d_1 = arr_1d[0] # First elemnet
el1d_1 = 8 # Edit element
arr_1d.append(7) # Add elemnet after last element
arr_1d.pop() # Remove Last Element

# 2D Array
arr_2d = [[1,2,3],[4,5,6]]

# Linked List
class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def print_list(head): # Linked list print function
    p = head
    while p != None:
        print(p.value)
        p = p.next

def append_list(head, value): # Linked list add function
    node = ListNode(value)
    if head == None:
        head = node
    else:
        p = head
        while p.next != None:
            p = p.next
        p.next = node
    return head

def get_node(head, index): # Get node value
    if index < 0:
        print("Please enter valid number")
        return
    p = head
    i = 0
    while i < index and p != None:
        p = p.next
        i += 1
    if p != None:
        print(p.value)
    else:
        print("Error")

def remove_node(head, value): # Remove node value
    p = head
    q = None
    while p!= None and p.value != value:
        q = p
        p = p.next
    if p == None:
        print("Node doesn't exist")
    else:
        if p == head:
            head = head.next
        else:
            q.next = p.next
    return head

# Stack
class Stack:
    def __init__(self):
        self.s =[]
    
    # Add element to stack
    def push(self, value):
        self.s.append(value)
    
    # Remove element from stack
    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.s.pop()
    
    # Is stack empty
    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False
    
    # Reture last element
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.s[-1] 

# Queue
class Queue:
    def __init__(self):
        self.q = []
    
    # Add element to queue
    def enqueue(self, value):
        self.q.append(value)

    # Remove elemnet from queue
    def dequeue(self):
        self.q.pop(0)

    # Return front(first element) in queue
    def front(self):
        return self.q[0]

# Recursion
def fact(x):
    if x == 0:
        return 1
    else:
        return (x * fact(x-1))
    
# Binary Search
def binary_search(data, value):
    l = 0
    h = len(data) - 1

    while l <= h:
        m =  (l + h) // 2
        if data[m] == value:
            return True
        elif data[m] > value:
            h = m - 1
        else: 
            l = m + 1

    return False

# Selection Sorting
def selection_sort(list):
    n = len(list)
    for i in range(n):
        index_min = i
        for j in range(i, n):
            if list[j] < list[index_min]:
                index_min = j
        list[index_min], list[i] = list[i], list[index_min]

# Bubble Sorting
def bubble_sort(arr):
    n= len(arr)
    permutation = True
    while permutation:
        permutation = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                permutation = True

# Insertion Sorting
def inertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] >arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1 

# Merge tow sorted arrays
def merge_two_lists(a,b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    result = []
    while i < n and j < m:
        if a[i] < b[j]:
            result.append(a[i])
            i = i + 1
    else:
            result.append(b[j])
            j = j + 1
    while i < n:
        result.append(a[i])
        i = i + 1
    while j < m:
        result.append(b[j])
        j = j + 1 

    return result