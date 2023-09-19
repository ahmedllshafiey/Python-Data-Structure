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

node_1 = ListNode(4) # Add value to node_1
node_2 = ListNode(1) # Add value to node_1
node_3 = ListNode(2) # Add value to node_1

node_1.next = node_2 # Add value next
node_2.next = node_3 # Add value next

head = node_1 # Creating head of list