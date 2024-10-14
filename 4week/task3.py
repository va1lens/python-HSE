"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                second: int = int(stack.pop())
                first: int = int(stack.pop())
                stack.append(int(first - second))
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "/":
                second: int = int(stack.pop())
                first: int = int(stack.pop())
                stack.append(int(first / second))
            else:
                stack.append(int(token))
        return stack[0]
