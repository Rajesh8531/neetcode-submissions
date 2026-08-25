class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if self.is_number(num):
                stack.append(num)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                val = self.calc(num,float(num2),float(num1))
                stack.append(val)
        return int(stack[0])

    def is_number(self,s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def calc(self,op,num1,num2):
        if op == '*':
            return num1 * num2
        elif op == '-':
            return num1 - num2
        elif op == '/':
            return int(num1/num2)
        return num1 + num2
        