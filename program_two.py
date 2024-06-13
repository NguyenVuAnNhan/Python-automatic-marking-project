'''
Interface of the exam
'''

import setup
import program_one
import sys

def assign_exam(Exam):
    try:
        fobj = open(Exam.path_to_dir+"/students.csv", "r")
    except:
        fobj = open(Exam.path_to_dir+"/students.csv", "w")
    candidates = setup.extract_students(fobj)  
    if len(candidates) == 0:
        print("No candidates found in the file")
        return None
    print("Assigning exam to candidates...")
    i = 0
    while i < len(candidates):
        candidates[i].exam = Exam.copy_exam()
        i += 1
    print(f"Complete. Exam allocated to {len(candidates)} candidates.")
    return candidates

def main(args):
    result = program_one.main(args)
    if result != None:
        candidates = assign_exam(result[0])
        while True:
            action = input("Enter SID to preview student's exam (-q to quit): ").strip()
            if action == "-a":
                i = 0
                while i < len(candidates):
                    print(candidates[i], end = "")
                    i += 1
            elif action == "-q":
                return candidates
                break
            else:
                is_valid_sid = action.isdigit() and len(action)==9
                if is_valid_sid:
                    sid_list = []
                    i = 0
                    while i < len(candidates):
                        sid_list.append(str(candidates[i].sid))
                        i += 1
                    try:
                        print(candidates[sid_list.index(action)], end = "")
                    except:
                        print("SID not found in list of candidates.\n")
                else:
                    print("SID is invalid.\n")
    else:
        return None




if __name__ == "__main__":
    main(sys.argv)
