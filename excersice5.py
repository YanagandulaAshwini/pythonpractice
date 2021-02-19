number=int(input("number of terms you want?"))
num1,num2=0,1
count=0
if number<=0:
    print("enter positive number")
elif number==1:
    print("fibonacci series up to:",number,":")
    print(num1)
else:
    print("fibonacci series:")
    while count<number:
           print(num1)
           num3=num1+num2
           num1=num2
           num2=num3
           count=count+1
