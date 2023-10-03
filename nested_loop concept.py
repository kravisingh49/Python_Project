#nested loop concept by designing a pyramid

i=1
while i<=5:
    j=1
    while j<=i:
        print("*", end='')
        j=j+1
    print()
    i=i+1;

## try the same concept but this i want to print numbers instead of "*".

i=1
while i<=5:
    j=1
    while j<=i:
        print(j, end='')
        j=j+1
    print()
    i=i+1;
##reverse this diagram now with same programing

i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end='')
        b=b+1
    j=1
    while j<=i:
        print("*",end='')
        j=j+1
    print()
    i=i+1;

