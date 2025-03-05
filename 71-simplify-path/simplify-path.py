class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        name = []
        for i in paths:
            if i:
                name.append(i)
        stack = []
        print(paths)
        for pa in name:
            print(pa)
            if pa == '.':
                continue
            elif stack and pa == '..':
                stack.pop()
            elif pa != '..':
                stack.append(pa)
        return '/' + '/'.join(stack)