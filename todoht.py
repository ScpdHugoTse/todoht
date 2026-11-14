# video 80
print("Your Personal Todo List!")
prompt = "Add, Show, Edit, Complete or Exit?"
todos = []
while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            file = open("todosht.txt", "r")
            todos = file.readlines()
            file.close()
            high_todo = todo.capitalize()
            todos.append(high_todo)
            file = open("todosht.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("todosht.txt", "r")
            todos = file.readlines()
            file.close()
            if len(todos) == 1:
                print("You have " + str(len(todos)) + " more task left on your list.")
            else:
                print("You have " + str(len(todos)) + " tasks left on your list.")
            placing = 0
            # ts makes sure taht i dont have an extra space cause \n makes it that u have an extra enter line but so does for loop so removing the \n here stops taht
            for i, f in enumerate(todos):
                f = f.strip("\n")
                print(f"Task {i+1}: {f.title()}")
        case "exit":
            print("Stopping program...")
            print("Program ended.")
            break
        case "complete":
            complet = int(input("What number on the list have you finished? "))
            if complet >= 1:
                print("Marking Task", complet, "as completed!")
                with open("todosht.txt", "r") as file:
                    file.writelines()
                complet = complet - 1
                del todos[complet]

            elif type(complet) == float:
                print("Can't be a decimal do it again...")
            else:
                print("That's under 1... it's not even on the list!")
        case "edit":
            file = open("todosht.txt", "r")
            todos = file.readlines()
            file.close()
            if len(todos) == 1:
                print("You have " + str(len(todos)) + " more task left on your list.")
            else:
                print("You have " + str(len(todos)) + " tasks left on your list.")
            placing = 0
            # ts makes sure taht i dont have an extra space cause \n makes it that u have an extra enter line but so does for loop so removing the \n here stops taht
            for i, f in enumerate(todos):
                f = f.strip("\n")
                print(f"Task {i + 1}: {f.title()}")
            number = int(input("Enter the number of the task that you want to edit:"))
            number = number - 1
            with open("todosht.txt", "r") as file:
                todos = file.readlines()

            edited = todos[number]
            change = input("What would you like to replace " + edited + " with?")
            todos[number] = change
            with open("todosht.txt", "w") as file:
                file.writelines(todos)
        case wrong:
            print("This doesn't fit any of the presented options. Try again.")
