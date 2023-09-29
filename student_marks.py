## write a program to calculate total marks in 5 subjects and maximum marks is 100
## and provide grading as well
##percentage>=80 - grade A    ##percentage>=40- grace C
##percentage>=60 - grade B    ##percentage<40- grade D

a = int(input("Enter English Marks:"))
b = int(input("Enter Hindi Marks:"))
c = int(input("Enter Maths Marks:"))
d = int(input("Enter Science Marks:"))
e = int(input("Enter Computer Marks:"))

total = a + b + c + d + e
percent = (total / 500) * 100
print("Total Marks =", total,",", "percentage =", percent)

if percent >= 80:
    print("You Got Grade A")
elif percent >= 60:
    print("You Got Grade B")
elif percent >= 40:
    print("You Got Grade C")
else:
    print("You Got Grade D");

        
        
    
