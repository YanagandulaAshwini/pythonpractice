number=int(input("enter the number:"))
sum=0
i=number
while i>0:
    digit=i%10
    sum+=digit**3
    i//=10
if number==sum:
    print(number, "is armstrong")
else:
    print(number,"is not armstrong")
