import random as random
num=random.randint(1,6)
count=0
while True:
     n=int(input("enter the number"))
     if n=num:
         print(f"u guessed in {count}attempts")
         count+=1
         break
    elif n>num:
        print("gssd num is greater")
        count+=1
    else:
        print("num is choosen smaller ")
    if count==3:
        print("lost all ur try")
        break

