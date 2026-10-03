# Find Minimum in Rotated Sorted Array

**Topic:** Binary Search  
**Difficulty:** Medium

## Problem

Given a sorted array that has been rotated between 1 and n times, find the minimum element.

## Example

### Input
`nums = [3,4,5,1,2]`

### Output
`1`

## Approach

Compare the middle element with the rightmost element to determine which half contains the minimum.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Interview Tip

Binary search can locate a boundary or extremum, not just an exact target.
