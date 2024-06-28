class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def peek(self):
        if self.head:
            return self.head.val
    
    def pop(self):
        if self.head:
            head_val = self.head.val
            self.head = self.head.next
            return head_val
    
    def is_empty(self):
        return self.head == None
    

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        astro_stack = LinkedListStack()
        ans_arr = []
        for astro in asteroids:
            
            while not astro_stack.is_empty() and astro < 0 and astro_stack.peek() > 0:
                if astro * -1 == astro_stack.peek():
                    astro_stack.pop()
                    break
                elif astro * -1 > astro_stack.peek():
                    astro_stack.pop()
                    continue
                else:
                    break
            else:
                astro_stack.push(astro)
        
        while not astro_stack.is_empty():
            ans_arr.append(astro_stack.pop())
        return ans_arr[::-1]
        