tasks = []

# print(len(tasks))

# tasks.append('revise quran')
# tasks.append('arabic language')
# tasks.append('workout')
# tasks.append('ai apprenticeship work')

# for task in tasks:
#     print(task)

while True:

    userchoice = input('1. Add Tasks   2. View Tasks   3.Delete Tasks   4. Exit')

    if userchoice == '1':
        print('ADD TASK/S')
        taskname = input('What is the name of your task?')
        
        tasks.append(taskname)
        for task in tasks:
            print(f"[{tasks.index(task) + 1}] - {task}")
        print('Task/s added!')
       

    elif userchoice == '2':
        print('VIEW TASKS')
        for task in tasks:
            print(f"[{tasks.index(task) + 1}] - {task}")
        print('Task/s in view!')
        
    elif userchoice == '3':
        print('DELETE TASK/S')
        for task in tasks:
            print(f"[{tasks.index(task) + 1}] - {task}")
        # print(len(tasks))
        deletechoice = int(input("Enter the number of the task you would like to delete:"))
        if deletechoice <= len(tasks):
            tasks.pop(deletechoice - 1)
            print('DELETE TASK/S')
            for task in tasks:
                print(f"[{tasks.index(task) + 1}] - {task}")
            print('task/s deleted!')

        else:
            print('incorrect input, the number you chose is out of range try again')
        

    elif userchoice == '4':
        print('Goodbye :(')
        break

    else:
        print('incorrect input, try again')


# print(type(userchoice))

    
    

    
