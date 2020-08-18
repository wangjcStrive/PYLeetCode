class Solution:
    def simplifyPath(self, path: str) -> str:
        result = ""
        subStr = ""
        lenth = len(path)
        stack =[]
        if lenth == 0:
            return result
        for i in range(1, lenth):
            if path[i] == '/':
                if subStr == "": # first #
                    continue
                else:
                    if subStr == "..":
                        if len(stack)>0:
                            stack.pop()
                    elif subStr == ".":
                        subStr = ''
                        continue
                    else:
                        stack.append(subStr)
                    subStr = ""
            else:
                subStr = subStr + path[i]

        if subStr !="":
            if subStr == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                if subStr != ".":
                    stack.append(subStr)
        if len(stack) == 0:
            return '/'
        else:
            for i in range(len(stack)):
                result = result + "/" + stack[i]
            return result

    def simplifyPath_1(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'': r, '.': r, '..': r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)

    def simplifyPath_2(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack: stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)


if __name__ == '__main__':
    input = [
        "/a//b////c/d//././/..",
        '/..',
        "/",
        "/home/.../abc/xyz",
        "/a/.",
        "/../",
        "/home/",
        "/../",
        "/home//foo/",
        "/a/./b/../../c/",
        "/a/../../b/../c//.//",
        "/a//b////c/d//././/.."
    ]
    ins = Solution()
    for path in input:
        print(ins.simplifyPath_1(path))