# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class ValidParentheses:

    # Runtime: 28 ms, faster than 85.59% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 13.7 MB, less than 91.84% of Python3 online submissions for Valid Parentheses.
    def isValid(self, s: str) -> bool:
        length = len(s)
        result = False
        if length == 0:
            return True
        if length%2 == 1:
            return False
        stack = []
        for str in s:
            if str == '(' or str == '[' or str=='{':
                stack.append(str)
            else:
                if len(stack) == 0:
                    result = False
                else:
                    if ((str == ')' and stack[-1]=='(')
                            or (str == ']' and stack[-1]=='[')
                            or (str=='}' and stack[-1]=='{')) :
                        stack.pop()
                        result = True
                    else:
                        result = False
        if len(stack)>0:
            result = False
        return result


if __name__ == '__main__':
    ins = ValidParentheses()
    print(ins.isValid(')('))
    print(ins.isValid('()[]{}'))
    print(ins.isValid('([)]'))
    print(ins.isValid('(]'))
    print(ins.isValid(''))
