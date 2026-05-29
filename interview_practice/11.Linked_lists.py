class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    # Initialize prev to None and curr to head
    # While curr is not None:
    #   Store curr.next in next_node (to avoid losing reference)
    #   Point curr.next to prev (reverse the link)
    #   Move prev to curr
    #   Move curr to next_node
    # Return prev (new head)
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev