def evaluate(string):
    string = string.replace(" ", "")

    def splitby(string, separators):

        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                lis.append(current)
                lis.append(ch)
                current = ""
            else:
                current += ch
        lis.append(current)
        return lis

    lis = splitby(string, "+-")

    def evaluate_mul_div(string):
        lis = splitby(string, "x/")
        if len(lis) == 1:
            return lis[0]
        
        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "x":
                output *= number

            elif operator == "/":
                output /= number

        return output

    
    for i in range(len(lis)):
        lis[i] = evaluate_mul_div(lis[i])

    output = float(lis[0])
    lis = lis[1:]

    while len(lis) > 0:
        operator = lis[0]
        number = float(lis[1])
        lis = lis[2:]

        if operator == "+":
            output += number
        elif operator == "-":
            output -= number

    return output

# Main Program
testcases = "1+2x3-4"
print(evaluate(testcases))

26. Largest 3 digit Palindrome

# Largest Palindrome
n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b
print(n)
27. Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"


def removeKdigits(num,k):    
    stack = []
    for digit in num:
        while k > 0 and len(stack) > 0 and stack[-1] > digit:
            k -= 1
            stack.pop()  
        stack.append(digit)
    if k > 0:
        stack = stack[:-k]     
    return "".join(stack).lstrip("0") or "0"

num="143219"
k=2
print(removeKdigits(num,k))

28. Return the Unicode of Uppercase letters

import string
import re
alphabets = list(string.ascii_uppercase)
for i in alphabets:
    print(i,"=",ord(i))
print(chr(65))
