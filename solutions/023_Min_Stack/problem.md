# Min Stack

**Topic:** Stack  
**Difficulty:** Medium

## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## Example

### Input
`push(-2), push(0), push(-3), getMin()`

### Output
`-3`

## Approach

Maintain a second stack containing the minimum value at each stack level.

## Complexity

- Time: `O(1) per operation`
- Space: `O(n)`

## Interview Tip

An auxiliary data structure can maintain additional state while preserving O(1) operations.
