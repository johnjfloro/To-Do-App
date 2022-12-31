def get_todos(filepath="todos.txt"):
    """Read & return list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """Write new todos to file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

