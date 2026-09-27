total_chores = 4
original_count = total_chores

print(f"You have {original_count} chores to do")

chores_completed = 0
chore_num = 1

while chore_num <= total_chores:

    if chore_num == 1: next_chore = "Make your bed"

    elif chore_num == 2: next_chore = "Feed the pet"

    elif chore_num == 3: next_chore = "Take out the trash"

    else:
        next_chore = "Wash the dish"

    answer = input(f"Have you finished: {next_chore}?(Yes/ No): ")

    if answer == "yes":

        chores_completed += 1

        chore_num += 1
        print("Great job. You have done the chores.")

    else:

        print("Complete the chores and check again")
                

    print("Remaining Chores =", total_chores - chores_completed)
    print()

test_value = 0

safety_counter = 0

while test_value <= 0:

    print("Condition will never end so it runs forvever.")

    safety_counter += 1

    if safety_counter == 3:
        print("Stop")
        break

print("========= Summary ==========")
print("Chores assigned today :", original_count)
print("Chores Completed today :", chores_completed)
print("Chores Remaining :", total_chores - chores_completed)
print("=" * 20)