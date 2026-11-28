# Top K Frequent Elements

**Topic:** Heap / Hashing  
**Difficulty:** Medium

## Problem

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Example

### Input
`nums = [1,1,1,2,2,3], k = 2`

### Output
`[1,2]`

## Approach

Count frequencies using an unordered_map. Maintain a min heap of size k based on frequency.

## Complexity

- Time: `O(n + m log k), where m is the number of distinct elements`
- Space: `O(n + k)`

## Interview Tip

Top K problems are classic candidates for a frequency map combined with a heap.
