'''
Interface of the exam
'''

import setup
import sys
import exam

def parse_cmd_args(args):
    '''
    Parameters:
        args: list, command line arguments
    Returns:
        result: None|tuple, details of the exam

    >>> parse_cmd_args(['program.py', '/home/info1110/', '60', '-r'])
    ('/home/info1110/', 60, True)

    >>> parse_cmd_args(['program.py', '/home/info1110/', 'ab', '-r'])
    Duration must be an integer

    >>> parse_cmd_args(['program.py', '/home/info1110/'])
    Check command line arguments
    '''
    try:
        a = False
        if len(args) < 3:
            print("Check command line arguments")
            return None
        if len(args) > 3 and args[3] == "-r":
            a = True
        if int(args[2]) <= 0:
            raise ValueError
        return (args[1], int(args[2]), a)
    except ValueError:
        print("Duration must be an integer")
        return None

def setup_exam(obj):
    '''
    Update exam object with question contents extracted from file 
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is setup successfully. Otherwise, False.
    '''
    obj.set_questions(setup.extract_questions(open(obj.path_to_dir+"/questions.txt", "r")))
    obj.set_exam_status()
    return (obj, obj.exam_status)

def main(args):
    '''
    Implement all stages of exam process.
    '''
    my_tuple = parse_cmd_args(args)
    if my_tuple == None:
        return None
    try:
        obj = exam.Exam(my_tuple[1], my_tuple[0], my_tuple[2])
        try:
            open(my_tuple[0]+"/questions.txt", "r")
            open(my_tuple[0]+"/students.csv", "r")
            print("Setting up exam...")
            result = setup_exam(obj)
            if result[1] == True:
                print("Exam is ready...")
                while True:
                    answer = input("Do you want to preview the exam [Y|N]? ").lower()
                    if answer == "y":
                        print(obj.preview_exam(), end="")
                    elif answer == "n":
                        return result
                        break
                    else:
                        print("Invalid command.")
            else:
                print("Error setting up exam")
        except FileNotFoundError:
            print("Missing files")
    except FileNotFoundError:
        print("Missing files")
        
    
        
if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)
