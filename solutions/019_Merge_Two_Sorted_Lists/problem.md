# Merge Two Sorted Lists

**Topic:** Linked List  
**Difficulty:** Easy

## Problem

Merge two sorted linked lists and return the head of the merged sorted list.

## Example

### Input
`list1 = [1,2,4], list2 = [1,3,4]`

### Output
`[1,1,2,3,4,4]`

## Approach

Use a dummy node and repeatedly attach the smaller current node from the two lists.

## Complexity

- Time: `O(n + m)`
- Space: `O(1)`

## Interview Tip

Dummy nodes simplify linked-list insertion and merging.
