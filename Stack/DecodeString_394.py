# 394. Decode String

# 2[a3[b]c]
# 12[a3[b]c]
# 2[ab3[c]]
# 两位数字/字符情况

# 遇到[的时候把前面存下的str/num push到对应stack中
# input 2[a3[b]c]
# strStack      numStack
#   a               3       -> a + 3 * b
#   ""              2       -> '' + 2 * res

# Runtime: 48 ms, faster than 17.39% of Python3 online submissions for Decode String.
# Memory Usage: 13.8 MB, less than 76.71% of Python3 online submissions for Decode String.
class DecodeString_394:
    def decodeString(self, s: str) -> str:
        result = ''
        strStack = []
        numStack = []
        num = 0
        for x in s:
            if '0' <= x <= '9':
                num = num*10 + int(x)
            elif 'a' <= x <= 'z' or 'A' <= x <= 'Z':
                result = result + x
            elif x == '[':
                numStack.append(num)
                num = 0
                strStack.append(result)
                result = ''
            elif x == ']':
                strStack[-1] = strStack[-1] + numStack[-1]*result
                result = strStack[-1]
                numStack.pop()
                strStack.pop()
        return result



if __name__ == '__main__':
    ins = DecodeString_394()
    print(ins.decodeString('2[a3[b]c]'))
    print(ins.decodeString('12[a3[b]c]'))
    print(ins.decodeString('2[ab3[c]]'))