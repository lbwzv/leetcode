class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        # 使用字典配对
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        #利用栈的性质 创建列表
        stack = list()
        for ch in s:
            if ch in pairs: #如果是右括号
                if not stack or stack[-1] != pairs[ch]: #空列表或不同为一种括号
                    return False
                else:
                    stack.pop() #删除栈顶
            else:
                stack.append(ch) #如果是左括号 在栈顶添加
        return not stack