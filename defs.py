
fp = "todos.txt"

def reading(filepath=fp):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def writing(todos, filepath = fp):
    with open(filepath, 'w') as file:
        file.writelines(todos)
    return todos

    