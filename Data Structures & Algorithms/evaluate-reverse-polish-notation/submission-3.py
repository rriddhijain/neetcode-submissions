class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch not in ('+-*/'):
                stack.append(int(ch))
            elif ch=="+":
                num1=int(stack.pop())
                num2=int(stack.pop())
                sum=num1+num2
                stack.append(sum)
            elif ch=="-":
                num1=int(stack.pop())
                num2=int(stack.pop())
                sum=num2-num1
                stack.append(sum)
            elif ch=="*":
                num1=int(stack.pop())
                num2=int(stack.pop())
                sum=num1*num2
                stack.append(sum)
            elif ch=="/":
                num1=int(stack.pop())
                num2=int(stack.pop())
                sum=int(num2/num1)
                stack.append(sum)
        t= int(stack.pop())
        return t
            

        