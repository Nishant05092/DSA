# Non-overlapping Intervals

**Topic:** Intervals / Greedy  
**Difficulty:** Medium

## Problem

Given an array of intervals, return the minimum number of intervals you need to remove to make the rest non-overlapping.

## Example

### Input
`intervals = [[1,2],[2,3],[3,4],[1,3]]`

### Output
`1`

## Approach

Sort intervals by ending time. Greedily select intervals that start at or after the ending time of the previously selected interval. Remove the rest.

## Complexity

- Time: `O(n log n)`
- Space: `O(1) auxiliary space excluding sorting`

## Interview Tip

For interval scheduling problems, sorting by ending time often leads to a greedy solution.
