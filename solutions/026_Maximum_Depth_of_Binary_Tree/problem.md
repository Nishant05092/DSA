# Maximum Depth of Binary Tree

**Topic:** Tree  
**Difficulty:** Easy

## Problem

Given the root of a binary tree, return its maximum depth.

## Example

### Input
`root = [3,9,20,null,null,15,7]`

### Output
`3`

## Approach

Use recursion. The depth of a node is one plus the maximum depth of its left and right subtrees.

## Complexity

- Time: `O(n)`
- Space: `O(h)`

## Interview Tip

Many tree problems can be expressed naturally using recursive subtree relationships.
