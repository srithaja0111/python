num1=int(input("enter the number:"))
choice=input("enter the symbol(+,-,*,/,%):")
num2=int(input("enter the number:"))
if choice=='+':
    print("result:",num1+num2)
elif choice=='-':
    print("result:",num1-num2)
elif choice=='*':
    print("result:",num1*num2)
elif choice=='/':
    print("result:",num1/num2)
elif choice=='%':
    print("result:",num1%num2)
else:
    ("invalid operation")
