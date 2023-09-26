str=input("Enter the shtring : ")
n=len(str)
reversed_str=""
for i in range(n-1,-1,-1):
    reversed_str=reversed_str+str[i]

if reversed_str==str:
    print(str+" is a palindrome string")
else:
    print(str+" is not a palindrome string")
