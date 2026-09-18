# Two Sum

**Topic:** Array  
**Difficulty:** Easy

## Problem

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## Example

### Input
`nums = [2,7,11,15], target = 9`

### Output
`[0,1]`

## Approach

Use a hash map to store previously seen numbers and their indices. For each number, check whether target - number already exists.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Interview Tip

Hashing can reduce the brute-force O(n²) solution to O(n).
