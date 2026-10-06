# Linked List Cycle

**Topic:** Linked List  
**Difficulty:** Easy

## Problem

Given the head of a linked list, determine if the linked list contains a cycle.

## Example

### Input
`head = [3,2,0,-4], tail connects to node index 1`

### Output
`true`

## Approach

Use Floyd's slow and fast pointer algorithm. If the pointers meet, a cycle exists.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Floyd's cycle detection algorithm is a fundamental linked-list technique.
