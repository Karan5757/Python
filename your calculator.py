print("Your Calculator")
num1= float(input("Write your first number: "))
op=input("Choose your operator: +,-,*,/ \n")
num2= float(input("Write your second number: "))
if op=="*":
    print(num1*num2)
elif op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
else:
    print("Error/Invlaid Operator")
