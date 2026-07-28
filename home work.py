total_homework = 4
original_count = total_homework
print(f"you have {original_count} homework task to finish today! \n")

completed_count = 0
task_num = 1

while task_num <= total_homework:
    if task_num == 1:
        next_task = "math worksheet"
    elif task_num == 2:
        next_task = "science reading"
    elif task_num == 3:
        next_task = "english writing"
    else:
        next_task = "coding pratice"

    answer = input(f"Have you finished: {next_task}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("great job! homework task completed.")
    else:
        print("okay, finish it and check again")

    print("homework task remaining: ", total_homework - completed_count)
    print()

print("=========All homework completed!=========")
print("great work finishing your homework today!")

print("now let's safely peek into an infinite loop...")
test_value = 0
safety_counter = 0

while test_value <= 0:
    print("this condition never changes, so this would run forever")

    if safety_counter == 5:
        print("stoping here on purpose - a real infinite never stops on its own")
        break

print("\n===== HOMEWORK COMPLETION SUMMARY =====")
print("Homework Assigned Today:", original_count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total_homework - completed_count)
print("=======================================")