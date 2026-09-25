# 3Sum

**Topic:** Two Pointers  
**Difficulty:** Medium

## Problem

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that their sum is zero.

## Example

### Input
`nums = [-1,0,1,2,-1,-4]`

### Output
`[[-1,-1,2],[-1,0,1]]`

## Approach

Sort the array and fix one element. Use two pointers for the remaining two elements while skipping duplicates.

## Complexity

- Time: `O(n²)`
- Space: `O(1) excluding output`

## Interview Tip

Sorting plus two pointers is a core pattern for pair and triplet problems.
