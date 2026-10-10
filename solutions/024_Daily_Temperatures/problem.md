# Daily Temperatures

**Topic:** Monotonic Stack  
**Difficulty:** Medium

## Problem

Given an array of daily temperatures, return an array where answer[i] tells how many days you have to wait after day i to get a warmer temperature.

## Example

### Input
`temperatures = [73,74,75,71,69,72,76,73]`

### Output
`[1,1,4,2,1,1,0,0]`

## Approach

Use a decreasing monotonic stack of indices. When the current temperature is greater than the temperature at the stack top, resolve that previous day.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Interview Tip

Monotonic stacks are useful for next greater/smaller element problems.
