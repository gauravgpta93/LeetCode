class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        in_value = {"(": ")", "[": "]", "{": "}"}
        out_value = [")", "]", "}"]
        for paranthesis in s:
            if paranthesis in in_value:
                stack.append(paranthesis)
            elif not len(stack) or paranthesis not in out_value:
                return False
            else:
                out = stack.pop()
                if in_value[out] != paranthesis:
                    return False
        return not len(stack)
