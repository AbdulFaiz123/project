#write a program to accept a number from user:then dislay#

num =int(input("enter the number"))
temp=num
rev=0

while num!=0:
     rev=rev*10+num%10
     num//=10

print(f"reverse of{temp}is{rev} ")
