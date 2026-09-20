# Maximum Subarray

**Topic:** Array  
**Difficulty:** Medium

## Problem

Given an integer array nums, find the subarray with the largest sum and return its sum.

## Example

### Input
`nums = [-2,1,-3,4,-1,2,1,-5,4]`

### Output
`6`

## Approach

Use Kadane's algorithm. Maintain the best sum ending at the current position and update the global maximum.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Kadane's algorithm is a must-know array pattern.
