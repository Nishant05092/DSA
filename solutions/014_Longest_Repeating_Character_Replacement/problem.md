# Longest Repeating Character Replacement

**Topic:** Sliding Window  
**Difficulty:** Medium

## Problem

Given a string s and an integer k, you can replace at most k characters. Return the length of the longest substring containing the same letter after replacements.

## Example

### Input
`s = "AABABBA", k = 1`

### Output
`4`

## Approach

Maintain a sliding window and the frequency of its most common character. If window size minus maximum frequency exceeds k, shrink the window.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

A useful sliding-window condition is window_size - most_frequent_count <= k.
