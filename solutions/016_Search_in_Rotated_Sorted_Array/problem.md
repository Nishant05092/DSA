# Search in Rotated Sorted Array

**Topic:** Binary Search  
**Difficulty:** Medium

## Problem

Given an array nums sorted in ascending order and rotated at an unknown pivot, search for target and return its index.

## Example

### Input
`nums = [4,5,6,7,0,1,2], target = 0`

### Output
`4`

## Approach

At every step one half of the array is guaranteed to be sorted. Determine which half is sorted and check whether the target belongs to that range.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Interview Tip

In rotated binary search, first identify which half is sorted.
