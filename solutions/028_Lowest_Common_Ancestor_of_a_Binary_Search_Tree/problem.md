# Lowest Common Ancestor of a Binary Search Tree

**Topic:** BST  
**Difficulty:** Medium

## Problem

Given a binary search tree and two nodes p and q, find their lowest common ancestor.

## Example

### Input
`root = [6,2,8,0,4,7,9], p = 2, q = 8`

### Output
`6`

## Approach

Use the BST ordering property. If both nodes are smaller, move left. If both are larger, move right. Otherwise the current node is the LCA.

## Complexity

- Time: `O(h)`
- Space: `O(1)`

## Interview Tip

Always look for properties of BSTs that can eliminate unnecessary traversal.
