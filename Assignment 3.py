# Part 1 -  Create a program that takes in a total of 5 tasks from the user
#           Each task should include both a task description, and duration in hours
#           If the total sum of durations in your task list exceeds 8 hrs, you must
#           ask the user which task they would like to remove, by index, from their
#           list, you should do this until the duration of the tasks in your list are
#           less than or equal to 8 hours

total_dur_hours = 0
task_list = []

task1_desc = input('Please input a task: ')
task1_duration = float(input('Please input the duration of the task: '))
task_list.append([task1_desc, task1_duration])
total_dur_hours = total_dur_hours + task1_duration

task2_desc = input('Please input a task: ')
task2_duration = float(input('Please input the duration of the task: '))
task_list.append([task2_desc, task2_duration])
total_dur_hours = total_dur_hours + task2_duration

task3_desc = input('Please input a task: ')
task3_duration = float(input('Please input the duration of the task: '))
task_list.append([task3_desc, task3_duration])
total_dur_hours = total_dur_hours + task3_duration

task4_desc = input('Please input a task: ')
task4_duration = float(input('Please input the duration of the task: '))
task_list.append([task4_desc, task4_duration])
total_dur_hours = total_dur_hours + task4_duration

task5_desc = input('Please input a task: ')
task5_duration = float(input('Please input the duration of the task: '))
task_list.append([task5_desc, task5_duration])
total_dur_hours = total_dur_hours + task5_duration

print('Yo homie, your total task hours is:', total_dur_hours)

if total_dur_hours > 8:
    print('Your task is greater then 8 hours')
    print(task_list)
    delete_task = int(input('Please choose a task to delete by index: '))
    popped_val = task_list.pop(delete_task)
    total_dur_hours = total_dur_hours - popped_val[1]
    print(total_dur_hours)    

if total_dur_hours > 8:
    print('Your tasks are still greater then 8 hours')
    print(task_list)
    delete_task = int(input('Please choose a task to delete by index: '))
    popped_val = task_list.pop(delete_task)
    total_dur_hours = total_dur_hours - popped_val[1]
    print(total_dur_hours)   

if total_dur_hours > 8:
    print('Your tasks are still greater then 8 hours')
    print(task_list)
    delete_task = int(input('Please choose a task to delete by index: '))
    popped_val = task_list.pop(delete_task)
    total_dur_hours = total_dur_hours - popped_val[1]
    print(total_dur_hours)   

if total_dur_hours > 8:
    print('Your tasks are still greater then 8 hours')
    print(task_list)
    delete_task = int(input('Please choose a task to delete by index: '))
    popped_val = task_list.pop(delete_task)
    total_dur_hours = total_dur_hours - popped_val[1]
    print(total_dur_hours)   

if total_dur_hours > 8:
    print('Your tasks are still greater then 8 hours')
    print(task_list)
    delete_task = int(input('Please choose a task to delete by index: '))
    popped_val = task_list.pop(delete_task)
    total_dur_hours = total_dur_hours - popped_val[1]
    print(total_dur_hours)   

else:
    print('Your task list does not exceed 8 hours')
    print(task_list)

# Part 2 

num_bags = int(input('Please input the number of bags you have: '))
ticket_type = input('Please input the ticket type you have from the following selection "First-Class", "Business-Class", or "Coach": ')
bag_fee = 0

if ticket_type == 'First-Class':
    ticket_price = 1000
    if num_bags <= 5:
        bag_fee = 0
    else:
        bag_fee = (num_bags - 5) * 20
elif ticket_type == 'Business-Class':
    ticket_price = 750
    if num_bags <= 2:
        bag_fee = 0
    elif num_bags == 3 or 4:
        bag_fee = (num_bags - 2) * 35
    else:
        bag_fee = (num_bags - 4) * 50
else:
    ticket_price = 500
    if num_bags <= 1:
        bag_fee = 0
    else:
        bag_fee = (num_bags - 1) * 75

total_ticket_price = ticket_price + bag_fee
total_ticket_price = float(total_ticket_price)
print('Your ticket type is:', ticket_type)
print('The number of bags you have is:', num_bags)
print('Your total ticket price is: ${0:.2f}'.format(total_ticket_price))
