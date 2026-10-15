# Validate Binary Search Tree

**Topic:** BST  
**Difficulty:** Medium

## Problem

Given the root of a binary tree, determine whether it is a valid binary search tree.

## Example

### Input
`root = [2,1,3]`

### Output
`true`

## Approach

Recursively maintain a valid range for each node. Every node must be strictly greater than its lower bound and smaller than its upper bound.

## Complexity

- Time: `O(n)`
- Space: `O(h)`

## Interview Tip

For BST validation, checking only immediate children is insufficient; maintain the full valid range.
