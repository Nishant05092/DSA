# Reverse Linked List

**Topic:** Linked List  
**Difficulty:** Easy

## Problem

Given the head of a singly linked list, reverse the list and return the reversed list.

## Example

### Input
`1 -> 2 -> 3 -> 4 -> 5`

### Output
`5 -> 4 -> 3 -> 2 -> 1`

## Approach

Use three pointers: previous, current, and next. Reverse each current node's pointer and move forward.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Always save curr->next before changing the pointer.
