def address(str):
     upper_case, lower_case, number, special_char = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_case += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower_case += 1
          elif str[i] >= '0' and str[i] <= '9': number += 1
          else: special_char += 1
     return upper_case, lower_case, number, special_char
           
str = "@WelCome@1234"
print("Original Substrings:",str)
u, l, n, s = address(str)
print('\nUpper case characters: ',u)
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)
