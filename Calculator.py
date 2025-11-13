a=int(input("enter first number : "))
b=int(input("enter second number : "))

c=input(str("enter symbol for the operation : "))

for i in c:
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
    else:
        break;


    

