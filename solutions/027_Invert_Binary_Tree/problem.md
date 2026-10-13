# Invert Binary Tree

**Topic:** Tree  
**Difficulty:** Easy

## Problem

Given the root of a binary tree, invert the tree and return its root.

## Example

### Input
`root = [4,2,7,1,3,6,9]`

### Output
`[4,7,2,9,6,3,1]`

## Approach

Recursively invert the left and right subtrees and then swap the two child pointers.

## Complexity

- Time: `O(n)`
- Space: `O(h)`

## Interview Tip

Think of tree recursion as solving the same problem independently for each subtree.
