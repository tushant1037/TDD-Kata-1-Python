# TDD-Kata-1-Python

## String Calculator Development Steps

1. **Add Method with Basic Support**  
   Create a method `Add(string)` that returns `0` for an empty string, and the sum of up to two comma-separated numbers.

2. **Handle Unknown Number of Inputs**  
   Extend the method to handle any number of comma-separated integers.

3. **Support Newlines as Delimiters**  
   Allow newlines (`\n`) as valid delimiters along with commas.  
   Example: `"1\n2,3"` should return `6`.

4. **Support Custom Single-Character Delimiters**  
   Add support for a custom delimiter using the format:  
   `"//[delimiter]\n[numbers...]"`  
   Example: `"//;\n1;2"` should return `3`.

5. **Throw Exception on Negative Numbers**  
   If any negative numbers are passed, raise a `ValueError` with the message:  
   `"negatives not allowed: -1, -4"` listing all negative numbers found.

6. **Ignore Numbers Greater Than 1000**  
   Any number greater than `1000` should be ignored in the sum.  
   Example: `"2,1001"` returns `2`.

7. **Support Delimiters of Any Length**  
   Allow custom delimiters of any length using this format:  
   `"//[***]\n1***2***3"` returns `6`.

8. **Support Multiple Delimiters**  
   Allow multiple custom delimiters using the format:  
   `"//[*][%]\n1*2%3"` returns `6`.

9. **Support Multiple Delimiters with Length > 1**  
   Support multiple delimiters where each can be longer than one character.  
   Example: `"//[***][%%][@@@]\n1***2%%3@@@4"` returns `10`.

