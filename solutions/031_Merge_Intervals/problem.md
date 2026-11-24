# Merge Intervals

**Topic:** Intervals  
**Difficulty:** Medium

## Problem

Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals and return an array of non-overlapping intervals.

## Example

### Input
`intervals = [[1,3],[2,6],[8,10],[15,18]]`

### Output
`[[1,6],[8,10],[15,18]]`

## Approach

Sort intervals by starting time. Iterate through them and merge the current interval with the last interval in the answer whenever they overlap.

## Complexity

- Time: `O(n log n)`
- Space: `O(n) excluding sorting space and output`

## Interview Tip

Whenever a problem involves overlapping ranges or time intervals, consider sorting by starting time.
