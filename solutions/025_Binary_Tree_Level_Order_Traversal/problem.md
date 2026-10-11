# Binary Tree Level Order Traversal

**Topic:** Tree  
**Difficulty:** Medium

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values.

## Example

### Input
`root = [3,9,20,null,null,15,7]`

### Output
`[[3],[9,20],[15,7]]`

## Approach

Use a queue for BFS. Process all nodes currently in the queue as one level before moving to the next level.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Interview Tip

BFS with a queue is the standard approach for level-order traversal.
