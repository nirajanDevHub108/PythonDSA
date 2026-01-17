def checkRedundancy(s):
    stack=[]
    n=len(s)
    
    for i in range(n):
        ch=s[i]
        if ch == ')':
            top = stack[-1] 
            stack.pop() 
            
            flag=True
            while top != '(':
                if top in {'+', '-', '*', '/'}: 
                    flag = False
                top = stack[-1]
                stack.pop()
            if flag:
                return True
        else:
            stack.append(ch)
    return False
    
    
s = "((a+b))"
print("true" if checkRedundancy(s) else "false")