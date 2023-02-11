#07-06-2021

# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4


print("Enter the oprands")
a=int(input())
b=int(input())
print("Enter the operator")
op= input()
if op== '-' :
    print(a-b)

elif op== '+':
    if a == 56 or 9  and b == 9 or 56:
        print("77")
    else:
        print(a+b)
elif op == '*':
    if a == 45 or 3 and b == 3 or 45:
        print("555")
    else:
        print(a * b)

elif op == '/':
    if a == 56 or 4  and b == 4 or 56:
        print("4")
    else:
        print(a/b)
else:
    print("Enter the correct operator")