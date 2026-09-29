# Longest Substring Without Repeating Characters

**Topic:** Sliding Window  
**Difficulty:** Medium

## Problem

Given a string s, find the length of the longest substring without repeating characters.

## Example

### Input
`s = "abcabcbb"`

### Output
`3`

## Approach

Use a sliding window with a frequency array or hash map. Expand the right pointer and move the left pointer when a duplicate appears.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Sliding window is essential for substring and subarray problems with constraints.
