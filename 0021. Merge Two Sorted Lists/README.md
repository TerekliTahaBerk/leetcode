# Merging Two Sorted Linked Lists in Python

## Introduction
In this document, we will explore a Python implementation that merges two sorted singly-linked lists into a single sorted linked list. This task is a common problem in data structures and algorithms, often encountered in coding interviews and competitive programming. The provided code efficiently combines the two lists while maintaining their sorted order.

## Key Concepts
Before diving into the code, let's clarify some key concepts:

- **Singly-Linked List**: A data structure consisting of nodes, where each node contains a value and a reference to the next node in the sequence. The last node points to `None`.
- **ListNode Class**: This class represents a single node in the linked list, containing a value (`val`) and a pointer to the next node (`next`).
- **Merging**: The process of combining two lists into one while preserving the order of elements.

## Code Structure
The code consists of a `Solution` class with a method `mergeTwoLists`. This method takes two linked lists as input and returns a new linked list that contains all the elements from both lists in sorted order. The merging process is done iteratively, using a dummy node to simplify the logic.

### Key Components:
- **Dummy Node**: A temporary node that acts as a placeholder to simplify the merging process.
- **Current Pointer**: A pointer that keeps track of the last node in the merged list.
- **While Loop**: This loop iterates through both lists, comparing their values and appending the smaller value to the merged list.

## Code Example
Here is the complete code for merging two sorted linked lists:

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()  # Create a temporary dummy node
        current = dummy  # Start with the dummy node

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move the current pointer forward

        # If there are remaining nodes in list1 or list2, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # Return the merged list, skipping the dummy node
```

## Explanation of the Code:
1. ListNode Class: Defines the structure of a node in the linked list.
2. mergeTwoLists Method:
	-	A dummy node is created to facilitate the merging process.
	-	A while loop runs as long as both lists have nodes. It compares the values of the current nodes from both lists and appends the smaller one to the merged list.
	-	After the loop, if any nodes remain in either list, they are appended directly to the merged list.
	-	Finally, the method returns the merged list starting from the node after the dummy.

## Conclusion
The provided code effectively merges two sorted linked lists into a single sorted linked list using a straightforward iterative approach. By utilizing a dummy node, the implementation simplifies the handling of edge cases, such as when one list is exhausted before the other. This method is efficient and maintains the sorted order of the elements, making it a valuable solution for problems involving linked lists.

