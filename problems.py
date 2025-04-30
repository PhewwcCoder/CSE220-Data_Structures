class ListNode:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

def createList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for elem in arr[1:]:
        current.next = ListNode(elem)
        current = current.next
    return head

def printList(head):
    current = head
    while current:
        print(current.elem, end="")
        if current.next:
            print(" --> ", end="")
        current = current.next
    print()

"""
Solve this using Recursion.
Input:
| List1: 1 → 2 → 6 → 8 → 11 → None    
| List2: 5 → 7 → 3 → 9 → 4 → None
Output:
| 1 → 5 → 2 → 7 → 6 → 3 → 8 → 9 → 11 → 4 → None |
"""

def alternate_merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    saved_head2_next = head2.next  # Save the next node of head2
    head2.next = head1.next        # Insert head2 into head1's list
    head1.next = head2             # Link head1 to head2

    # Recurse with the next nodes
    alternate_merge(head2.next, saved_head2_next)

    return head1

# Test Case
print("===============Test Case 1============")
head1 = createList([1, 2, 6, 8, 11])
head2 = createList([5, 7, 3, 9, 4])

print("Linked List 1:")
printList(head1)
print("Linked List 2:")
printList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printList(head)  # Expected: 1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4