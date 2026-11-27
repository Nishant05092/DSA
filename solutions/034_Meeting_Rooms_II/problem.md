# Meeting Rooms II

**Topic:** Intervals / Heap  
**Difficulty:** Medium

## Problem

Given an array of meeting time intervals, find the minimum number of conference rooms required.

## Example

### Input
`intervals = [[0,30],[5,10],[15,20]]`

### Output
`2`

## Approach

Sort meetings by starting time and maintain a min heap of ending times. Remove meetings that have already finished before assigning a room to the next meeting.

## Complexity

- Time: `O(n log n)`
- Space: `O(n)`

## Interview Tip

A min heap is useful when you need to efficiently track the earliest finishing task or meeting.
