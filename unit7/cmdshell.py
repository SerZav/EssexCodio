''' Interactive shell with python'''
import os
# use the os module for directory functions
from cmd import Cmd
# use the cmd module for shell framework

class cli(Cmd):
    ''' Main class that inherits from Cmd module '''
    prompt = os.getcwd() + "$>"
    def do_list(self, inp):
        '''SYNOPSIS:\
           \n   list [file]\
           \nDESCRIPTION:\
           \n   List files in specified directory.\
           \n   By default, list current directory.
        '''
        if not inp:
            # if no parameters, list current directory
            directory = os.listdir()
        else:
            # list directory
            try:
                directory = os.listdir(inp)
            except:
                print(f"Error: parameter '{inp}' is not a valid directory or file ")
                return
        for file in directory:
            print(file)


    def do_exit(self, inp):
        '''SYNOPSIS:\
           \n   exits shell '''
        return True

    def do_quit(self, inp):
        '''SYNOPSIS:\
           \n   exits shell '''
        return True        

    def do_clear(self, inp):
        os.system('clear')

    def do_add(self, inp):
        '''SYNOPSIS:\
           \n   add n [n2]... [n]\
           \nDESCRIPTION:\
           \n   add numbers included as parameters'''
        values = inp.split(' ')
        result = 0
        for value in values:
            if not value.isnumeric():
                print("ERROR: values must be numeric")
                return
            result += int(value)
        print(result)

    def default(self, inp):
        print("Command not found. Type 'Help' for a list of valid commands.")

if __name__ == '__main__':
    cli().cmdloop()
