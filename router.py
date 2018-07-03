from command import app

@app.route([], cmd='ls')
def list_path(args):
    """
    list current path files and directory
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['-f'], cmd='ls')
def list_files(args):
    """
    list the given files
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['-s'], cmd='ls')
def list_sorted_path(args):
    """
    list the current path and display them in order
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['-d'], cmd='ls')
def list_directory(args):
    """
    list current path directory
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['-s', '-d'], cmd='ls')
def list_sorted_directory(args):
    """
    list the current directory in order
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['-s', '-f'], cmd='ls')
def list_sorted_files(args):
    """
    list the current path files in order
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['-s', '-l'], cmd='ls')
def list_sorted_detail(args):
    """
    list the files detail in order
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route([], cmd='cd')
def change_directory(args):
    """
    change the directory
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route([], cmd='mkdir')
def create_directory(args):
    """
    create new directory
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route([], cmd='rm')
def remove_file(args):
    """
    just remove files
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['-r'], cmd='rm')
def remove_directory(args):
    """
    recursive remove files from directory
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route([], cmd='touch')
def touch_file(args):
    """
    create a new empty file
    """
    raise NotImplementedError("Not Implememnted Yet")

@app.route(['404'], cmd='error')
def cmd_not_found(args):
    """
    error handle function
    command not found error
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['200'], cmd='error')
def cmd_argument_error(args):
    """
    error handle function
    command argument not valid
    """
    raise NotImplementedError("Not Implemented Yet")

@app.route(['500'], cmd='error')
def switch_path_error(args):
    """
    error handle function
    """
    print("`{}` is not a valid path".format(args))

if __name__ == "__main__":

    app.run('touch file file2')