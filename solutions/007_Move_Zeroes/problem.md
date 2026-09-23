# Move Zeroes

**Topic:** Array  
**Difficulty:** Easy

## Problem

Given an integer array nums, move all zeroes to the end while maintaining the relative order of the non-zero elements.

## Example

### Input
`nums = [0,1,0,3,12]`

### Output
`[1,3,12,0,0]`

## Approach

Use a pointer to place non-zero elements at the front, then fill the remaining positions with zeroes.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

The slow-fast pointer pattern is common in array problems.
