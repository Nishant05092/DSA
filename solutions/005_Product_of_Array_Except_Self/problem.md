# Product of Array Except Self

**Topic:** Array  
**Difficulty:** Medium

## Problem

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements of nums except nums[i].

## Example

### Input
`nums = [1,2,3,4]`

### Output
`[24,12,8,6]`

## Approach

Build prefix products from the left and multiply them with suffix products from the right without using division.

## Complexity

- Time: `O(n)`
- Space: `O(1) excluding output`

## Interview Tip

Prefix and suffix techniques are useful when an answer depends on all elements except the current one.
