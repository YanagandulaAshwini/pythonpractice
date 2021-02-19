print("Please provide multiple sets of binary numbers that are comma separated: ")
binary_numbers = input()
 
numbers = [x for x in binary_numbers.split(',')]
binary_divisible_by_5 = []
 
for b in numbers:
    binary_int = int(b, 2)
    if not binary_int % 5:
        binary_divisible_by_5.append(b)
 
print("The list of numbers that are divisible by 5: ")
print(','.join(binary_divisible_by_5))
