# Best Time to Buy and Sell Stock

**Topic:** Array  
**Difficulty:** Easy

## Problem

Given an array prices where prices[i] is the price of a stock on the ith day, find the maximum profit that can be achieved by buying on one day and selling on a later day.

## Example

### Input
`prices = [7,1,5,3,6,4]`

### Output
`5`

## Approach

Maintain the minimum price seen so far and calculate the maximum profit at every day.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Track the minimum value seen so far instead of checking every pair.
