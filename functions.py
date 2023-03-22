def get_todos(filepath='todos.txt'):  # default parameter argument
    """ Read a text file and return the list of
    to do items"""
    with open(filepath, 'r') as file:  # with-context-manager
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_arg, filepath='todos.txt'):  # always use non default parameter before default para meter
    """Write the to-do items into the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# this will be executed only for this file not for other where you have imported this function file

if __name__ == '__main__':
    print("Hello")
    print(get_todos())
