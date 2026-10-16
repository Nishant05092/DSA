# Kth Smallest Element in a BST

**Topic:** BST  
**Difficulty:** Medium

## Problem

Given the root of a binary search tree, return the kth smallest value among all the node values.

## Example

### Input
`root = [3,1,4,null,2], k = 1`

### Output
`1`

## Approach

An inorder traversal of a BST visits nodes in sorted order. Stop when the kth node is visited.

## Complexity

- Time: `O(h + k)`
- Space: `O(h)`

## Interview Tip

Remember: inorder traversal of a BST produces values in sorted ascending order.
