from data.task_list import *


def get_uncompleted_tasks(list):

    total = 0
    for i in list:
        if i["completed"] == False:
            total += 1

    return total

# Get a list of completed tasks


def get_completed_tasks(list):

    total = 0
    for i in list:
        if i["completed"] == True:
            total += 1

    return total

# Get tasks where time_taken is at least a given time
# want to have a minimum time taken to do a task >=


def get_tasks_taking_at_least(list, time):

    new_list = []
    for i in list:
        if i["time_taken"] >= time:
            new_list.append(i)
    return new_list


print(get_tasks_taking_at_least(tasks, 30))

# Find a task with a given description


def get_task_with_description(list, description):

    new_list = []
    for i in list:
        if i["description"] == description:
            new_list.append(i)
    return new_list


print(get_task_with_description(tasks, "good boy dog"))

# Extention (Function):

# Get a list of tasks by status


def get_tasks_by_status(list, status):
    new_list = []

    for i in list:
        if i["completed"] == status:
            new_list.append(i)

    return new_list


def mark_task_complete(task):
    task["completed"] = True


def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task


def add_to_list(list, task):
    list.append(task)
