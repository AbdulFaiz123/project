#1.	Write a program to generate a fancy number for a new vehicle considering the following constraints:
#a.	The fancy number should have 4-digits.
#b.	The sum of these 4-digits should be 12.
#c.	The 3rd digit should be equal to the difference between the 1st and the 2nd digit.
#d.	The 4th digit should be equal to the sum of the 1st and the 3rd digit
def sum_digits(num):
    if num>10:
        return num
    s=0
    while num !=0:
        s+= num % 10
        num // =10
    return s