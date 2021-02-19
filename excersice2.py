name= "AShwini" 
upper=[]
lower=[]
for char in name:
    if char.lower():
        lower.append(char)
    else:
        upper.append(char)
sortedstring=' '.join(lower+upper)
print("arranging characters giving precedence to lowercase letters:")
print(sortedstring)
