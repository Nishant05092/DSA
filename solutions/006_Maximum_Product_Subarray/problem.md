# Maximum Product Subarray

**Topic:** Array  
**Difficulty:** Medium

## Problem

Given an integer array nums, find a contiguous non-empty subarray that has the largest product and return the product.

## Example

### Input
`nums = [2,3,-2,4]`

### Output
`6`

## Approach

Track both the maximum and minimum product ending at each position because a negative number can turn the minimum into the maximum.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

When multiplication and negative values are involved, track both maximum and minimum states.
