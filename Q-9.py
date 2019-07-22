#9.	Write a program to accept a five-digit number, increment each digit by 1 and then display the new number formed. Note that digit 9 gets incremented to 0.
#Example:
#Input: 14389
#Output: 25490


max=6
for i in range(1,max+1):
  for j in range(max,i-1,-1):
    print(" "end ="")
  for k in range(1,i+1):
      print("k",end ="")