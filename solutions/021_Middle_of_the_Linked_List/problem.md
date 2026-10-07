# Middle of the Linked List

**Topic:** Linked List  
**Difficulty:** Easy

## Problem

Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.

## Example

### Input
`head = [1,2,3,4,5]`

### Output
`[3,4,5]`

## Approach

Use slow and fast pointers. Slow moves one step while fast moves two steps. When fast reaches the end, slow is at the middle.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Slow-fast pointers can solve many linked-list problems in one pass.
