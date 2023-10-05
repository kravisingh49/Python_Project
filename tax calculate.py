##find tahe taxes you have to pay on your income.
print("Hello there, what is your income ?")

income=int(input("\nEnter your salary:\n\t"))

if income<=0:
    taxes=0
    print("you need the assistance from the welfare department")
    print("we are with you")
elif income > 0 and income < 9950:
    taxes = income * 0.1
elif income <= 9950 and income < 40525:
    taxes = income * 0.12
elif income <= 40525 and income < 86375:
    taxes = income * 0.22
elif income <= 86375 and income < 164925:
    taxes = income * 0.24
elif income <= 164925 and income < 209425:
    taxes = income * 0.32
elif income <= 209425 and income < 523600:
    taxes = income * 0.35

else:
    print("\nsomething is wrong, you did not enter the correct number\n")
print(f"\nyou are liable to pay an amount of ${taxes} in taxes\n")
