#08-06-2021
#Program to guess the number
num=29
print("********START********")
i=0
while(1):
    print("\nYou have",5-i,"Chance left")
    print("Enter Your Number")
    j=int(input())
    if j == num:
        print("*****You Won****")
        break
    if i==4:
        print("GAME OVER!")
        break
    if j<num:
        print("Increase your input")
        i=i+1
        continue
    elif(j>num):
        print("Decrease Your input")
        i = i + 1
        continue
    else:
        print("Enter A valid input")
