from command import app

@app.route([], cmd='ls')
def list_path(args):
    """
    list current path files and directory
    """
    print("list path", args)
    #raise NotImplementedError("Not ImplementedError")

@app.route(['200'], cmd='error')
def list_files(args):
    """
    list the given files
    """
    print("command not found")
    #raise NotImplementedError("Not ImplementedError")

@app.route(['-s'], cmd='ls')
def list_sorted_files(args):
    """
    list the current path and display them in order
    """
    #raise NotImplementedError("Not ImplementedError")
    print("list sorted files")

if __name__ == "__main__":

    app.run('lt -s')