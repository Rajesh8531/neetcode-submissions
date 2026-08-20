class Solution:
    def isValid(self, s: str) -> bool:
        mapper = { "}" : "{", "]" : "[", ")" : "(" }
        stack = []
        for ch in s:
            if ch == "{" or ch == "[" or ch == "(":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if item != mapper.get(ch,''):
                    return False
        return len(stack) == 0
        