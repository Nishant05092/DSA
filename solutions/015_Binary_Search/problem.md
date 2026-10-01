# Binary Search

**Topic:** Binary Search  
**Difficulty:** Easy

## Problem

Given a sorted array of integers nums and an integer target, return the index of target if it exists, otherwise return -1.

## Example

### Input
`nums = [-1,0,3,5,9,12], target = 9`

### Output
`4`

## Approach

Maintain a search range using left and right pointers. Compare the middle element with the target and eliminate half of the search space.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Interview Tip

Know both the standard binary search template and how to avoid integer overflow in mid calculation.
