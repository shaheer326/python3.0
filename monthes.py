months = [
    "January", "February", "March", "April", 
    "May", "June", "July", "August", 
    "September", "October", "November", "December"
]

ent = input("Do you want to know all the months (yes or no): ").lower()

if ent == "yes":
    for month in months:
        print(month)
elif ent == "no":
    pass
else:
    print("wrong input")