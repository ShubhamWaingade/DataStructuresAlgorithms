class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
class LinkedListStack:
    def __init__(self):
        self.head = None
        
    def push_node(self, value):
        current_node = Node(value)
        if self.head:
            current_node.next = self.head
        self.head = current_node
    
    def pop_node(self):
        stack_val = self.head.value
        self.head = self.head.next
        return stack_val
    
    def is_empty(self):
        return self.head == None
    

class Solution:
    def isValid(self, s: str) -> bool:
        string_stack = LinkedListStack()
        
        for ele in s:
            if ele == '{' or ele == '(' or ele == '[':
                string_stack.push_node(ele)
            else:
                if string_stack.is_empty():
                    return False
                stack_ele = string_stack.pop_node()
                if ele == '}' and stack_ele != '{':
                    return False
                if ele == ')' and stack_ele != '(':
                    return False
                if ele == ']' and stack_ele != '[':
                    return False
        if string_stack.is_empty():
            return True
        else:
            return False
        