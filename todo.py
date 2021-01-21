import sys   #Used this module for manipulating python runtime environment.
import os    #Used this module for file handling
from datetime import datetime


def help(): # This function is used to print the help menu
    todohelp = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
$ ./todo clearAll         # This clears the todo list"""
    sys.stdout.buffer.write(todohelp.encode(
        'utf8'))  # This writes utf8 to standard output

def add(st):
    # This function adds a new task to the todos
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFileList:
            data = todoFileList.read()
        with open("todo.txt", 'w') as todoFileMod:
            todoFileMod.write(st + '\n' + data)
    else:  # If not then creates a new file and adds the task.
        with open("todo.txt", 'w') as todoFile:
            todoFile.write(st + '\n')
    print('Added todo: "{}"'.format(st))


def ls():
    # This function lists available todos
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFile:   #open todo.txt in read mode
            availableTodos = todoFile.readlines()
        fileLength = len(availableTodos)
        outputString = ""
        for line in availableTodos:
            outputString += '[{}] {}'.format(fileLength, line)
            fileLength -= 1
        sys.stdout.buffer.write(outputString.encode(
            'utf8'))  # This writes utf8 to standard output in a reverse order
    else:
        print("There are no pending todos!")


def delete(num):
    # Function to Delete the task from the List. (If available)
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFileList:
            data = todoFileList.readlines()
        ct = len(data)
        if num > ct or num <= 0:
            print(f"Error: todo #{num} does not exist. Nothing deleted.")
        else:
            with open("todo.txt", 'w') as todoFileMod:
                for line in data:
                    if ct != num:
                        todoFileMod.write(line)
                    ct -= 1
            print("Deleted todo #{}".format(num))
    else:
        print("Error: todo #{} does not exist. Nothing deleted.".format(num))


def done(num):
    # Function to mark the given task as Done. (If available)
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFileList:
            data = todoFileList.readlines()
        ct = len(data)
        if num > ct or num <= 0:
            print("Error: todo #{} does not exist.".format(num))
        else:
            with open("todo.txt", 'w') as todoFileMod:
                if os.path.isfile('done.txt'):  # Produces output according to the availability of done.txt file.
                    with open("done.txt", 'r') as doneFileOri:
                        doneData = doneFileOri.read()
                    with open("done.txt", 'w') as doneFileMod:
                        for line in data:
                            if ct == num:
                                doneFileMod.write("x " + datetime.today().strftime('%Y-%m-%d') + " " + line)
                            else:
                                todoFileMod.write(line)
                            ct -= 1
                        doneFileMod.write(doneData)
                else:
                    with open("done.txt", 'w') as doneFileMod:
                        for line in data:
                            if ct == num:
                                doneFileMod.write("x " + datetime.today().strftime('%Y-%m-%d') + " " + line)
                            else:
                                todoFileMod.write(line)
                            ct -= 1

            print("Marked todo #{} as done.".format(num))
    else:
        print("Error: todo #{} does not exist.".format(num))


def report():
    # Function to Generate the Report.
    countTodo = 0
    countDone = 0
    if os.path.isfile('todo.txt'):
        with open("todo.txt", 'r') as todoFile:
            todoData = todoFile.readlines()
        countTodo = len(todoData)
    if os.path.isfile('done.txt'):
        with open("done.txt", 'r') as doneFile:
            doneData = doneFile.readlines()
        countDone = len(doneData)
    st = datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(countTodo, countDone)
    sys.stdout.buffer.write(st.encode('utf8'))

def clearAll():
    # Function to clear the todo list
    print("This clear all the todos")
    if os.path.isfile('todo.txt'):
        todoFile= open("todo.txt","r+")
        todoFile.truncate(0)
        todoFile.close()



if __name__ == "__main__":
    # sys.argv is used to retrieve command line arguments.
    # sys.argv[0] is the name of the program, this means if the user has just passed ./todo, help menu should appear.
    if len(sys.argv) == 1 or sys.argv[1] == 'help':
        help()
    elif sys.argv[1] == 'ls':
        ls()
    elif sys.argv[1] == 'add':
        if len(sys.argv) > 3:  # len(sys.argv) should be 3 for successful adding operation.
            print(
                "Error: You haven't used proper syntax for adding tasks, the tasks should be entered in double quotes")
        elif len(sys.argv) == 3:
            add(sys.argv[2])
        else:
            print("Error: Missing todo string. Nothing added!")
    elif sys.argv[1] == 'del':
        if len(sys.argv) > 2:
            delete(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for deleting todo.")
    elif sys.argv[1] == 'done':
        if len(sys.argv) > 2:
            done(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for marking todo as done.")
    elif sys.argv[1] == 'report':
        report()
    elif sys.argv[1] == 'clearAll':
        clearAll()
    else:
        print('Option Not Available. Please use "./todo help" for Usage Information')
