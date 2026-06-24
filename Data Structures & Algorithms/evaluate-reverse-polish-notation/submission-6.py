class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if stack:
                if tokens[i]=="+":
                    a=int(stack.pop())
                    b=int(stack.pop())
                    res= a+b
                    stack.append(res)
                elif tokens[i]=="-":
                    a=int(stack.pop())
                    b=int(stack.pop())
                    res=b-a
                    stack.append(res)
                elif tokens[i]=="*":
                    a=int(stack.pop())
                    b=int (stack.pop())
                    res=a*b
                    stack.append(res)
                elif tokens[i]=="/":
                    a=int(stack.pop())
                    b=int(stack.pop())
                    res=int(b/a)
                    stack.append(res)
                else:
                    c=int(tokens[i])
                    stack.append(c)
            else:
                c=int(tokens[i])
                stack.append(c)
        return stack.pop()

            
            