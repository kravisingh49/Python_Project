##write a program to find a sum of given digits.
n=int(input("enter number to add:"))
sum=0

while(n>0):
    sum=sum+(n%10)
    n=n//10
print("sum of digits=",sum);

##write a program to find sum of square of digits of given number.

n=int(input("enter number to sum of sqaure:"))
sum=0

while(n>0):
    sum=sum+(n%10)*(n%10)
    n=n//10
print("sum of square of digits=",sum);

##write a program to find sum of cube of digits of a given number.

n=int(input("enter number to sum of cube:"))
sum=0

while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
print("sum of cube of digits=",sum);

##write a program to check whether a given number is armstrong or not.

n=int(input("enter number to check armstrong or not:"))
sum=0
orig=n

while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if orig==sum:
    print("digit is armstrong number.")
else:
    print("digit is not armstrong number.");

##write a program to find product of given number.

n=int(input("enter number to product:"))
prod=1

while(n>0):
    prod=prod*(n%10)
    n=n//10
print("The results of product of digits=",prod);

##write a program to find a sum of even digits and product of odd digits.

n = int(input("Enter a number to find the sum of even digits and product of odd digits:"))
sum_even = 0
product_odd = 1

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_even += digit
    else:
        product_odd *= digit
    n //= 10

print("Sum of even digits:", sum_even)
print("Product of odd digits:", product_odd)

##write a program to check whether a number is palindrome or not.

n=int(input("enter number to check:"))
rev=0
x=n

while(n>0):
    rev=(rev*10)+(n%10)
    n=n//10
if rev==x:
    print("number is palindrome:")
else:
    print("number is not palindrome:")
