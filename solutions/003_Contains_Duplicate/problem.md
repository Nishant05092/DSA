# Contains Duplicate

**Topic:** Array  
**Difficulty:** Easy

## Problem

Given an integer array nums, return true if any value appears at least twice and false if every element is distinct.

## Example

### Input
`nums = [1,2,3,1]`

### Output
`true`

## Approach

Use an unordered_set. While traversing the array, if an element already exists in the set, a duplicate is present.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Interview Tip

A hash set provides average O(1) lookup.
