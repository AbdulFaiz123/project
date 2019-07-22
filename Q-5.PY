#5.	Write a program to print the Fibonacci series up to the number 34. #
a=0
b=1
c=0
print(a,b,end=" ")
while not c==34:
    c=a+b
    print(c,end=" ")
    a,b=b,c
