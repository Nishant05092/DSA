# Valid Parentheses

**Topic:** Stack  
**Difficulty:** Easy

## Problem

Given a string containing parentheses, determine if the input string is valid. Every opening bracket must be closed by the same type of bracket in the correct order.

## Example

### Input
`s = "()[]{}"`

### Output
`true`

## Approach

Use a stack. Push opening brackets and ensure every closing bracket matches the top of the stack.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Interview Tip

Stacks are ideal when the latest unmatched opening element must be processed first.
