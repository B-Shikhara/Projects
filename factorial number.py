#A program to print the factorial of a number

#to get the data from the user
n=int(input("Enter the Number: "))

fact=1 

for i in range(1,n+1):
    fact=fact*i
print("The factorial of",n,"is:",fact)
