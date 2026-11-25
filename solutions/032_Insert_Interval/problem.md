# Insert Interval

**Topic:** Intervals  
**Difficulty:** Medium

## Problem

Given a collection of non-overlapping intervals sorted by starting time and a new interval, insert the new interval and merge if necessary.

## Example

### Input
`intervals = [[1,3],[6,9]], newInterval = [2,5]`

### Output
`[[1,5],[6,9]]`

## Approach

Add all intervals that end before the new interval. Merge all overlapping intervals with the new interval. Finally, add the remaining intervals.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Interview Tip

Divide interval processing into three phases: before, overlapping, and after.
