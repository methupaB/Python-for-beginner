def calculater(x,y,z):
    if z == "+":
        ans = x + y

    elif z == "-":
        ans = x - y

    elif z == "/":
        ans = x / y

    elif z == "*":
        ans = x * y
          
    else:
        ans = ('Invaild !')

    return ans 
  

n1 = int(input("Enter Number 1:"))
n2 = int(input("Enter Number 2:"))
op = str(input("Operation  is(+,-,/,*):"))

ans = calculater(n1,n2,op)

print(f'The Answer is:{ans}')
