# Valid Palindrome

**Topic:** String  
**Difficulty:** Easy

## Problem

Given a string s, determine if it is a palindrome considering only alphanumeric characters and ignoring cases.

## Example

### Input
`s = "A man, a plan, a canal: Panama"`

### Output
`true`

## Approach

Use two pointers from both ends, skipping non-alphanumeric characters and comparing lowercase characters.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Interview Tip

Two pointers are often the simplest solution for palindrome problems.
