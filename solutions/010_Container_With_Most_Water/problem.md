# Container With Most Water

**Topic:** Two Pointers  
**Difficulty:** Medium

## Problem

Given an integer array height, find two lines that together with the x-axis form a container containing the most water.

## Example

### Input
`height = [1,8,6,2,5,4,8,3,7]`

### Output
`49`

## Approach

Start with pointers at both ends. Calculate the area and move the pointer with the smaller height.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

When maximizing distance-based pair values, consider whether two pointers can eliminate impossible candidates.
