print("Your Calculator")
num1= float(input("Write your First Number: "))
op=input("Choose any operator: +,-,*,/ \n")
num2= float(input("Write your Second number: "))
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
