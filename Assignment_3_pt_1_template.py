task_list = []
duration = 0

task_1_desc = input("Input task 1 description: ")
task_1_duration = float(input("Input task 1 duration: "))
task_list.append([task_1_desc, task_1_duration])
duration = duration + task_1_duration
# Add 4 more tasks




if duration > 8:
    print("Total Duration:", duration)
    print(task_list)
    remove = int(input("Task list is over 8 hours, which task would you like to remove?"))
    popped_val = task_list.pop(remove)
    duration = duration - popped_val[1]

# Add logic to check if after you remove the task the duration is over 8 hours,
# Think about how many times you should ask this question to the user



print("Total duration of tasks:", duration)
print(task_list)


