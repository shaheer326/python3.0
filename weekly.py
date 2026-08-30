weekly = ("Exercise", "Work", "Eat")
done = 0

while done < 3:
    daily = input(f"Have you done your tasks '{weekly[done]}' yes or no: ")
    
    if (daily=="yes"):
        done+=1
