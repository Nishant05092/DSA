# Majority Element

**Topic:** Array  
**Difficulty:** Easy

## Problem

Given an array nums of size n, return the majority element. The majority element appears more than n/2 times.

## Example

### Input
`nums = [2,2,1,1,1,2,2]`

### Output
`2`

## Approach

Use Boyer-Moore Voting Algorithm. Maintain a candidate and count, cancelling different elements against the candidate.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Boyer-Moore is an important O(1) space voting technique.
