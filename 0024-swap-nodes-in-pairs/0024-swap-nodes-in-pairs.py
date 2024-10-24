# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = ListNode(0, head)
        current_node = head
        previous_node = temp_head

        while current_node and current_node.next:
            next_pair_node = current_node.next.next
            second_node = current_node.next

            current_node.next = next_pair_node
            second_node.next = current_node
            previous_node.next = second_node

            previous_node = current_node
            current_node = next_pair_node
        return temp_head.next