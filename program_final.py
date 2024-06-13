'''
Interface of the exam
'''

import setup
import program_two

def check_sid_ls(ls):
    i = 0
    return_ls = []
    while i < len(ls):
        return_ls.append(ls[i].sid)
        i += 1
    return return_ls

def check_name_ls(ls):
    i = 0
    return_ls = []
    while i < len(ls):
        return_ls.append(ls[i].name.lower())
        i += 1
    return return_ls 


def main(args):
    candidates = program_two.main(args)
    if candidates == None:
        return None
    else:
        tries = 0
        while tries < 3:
            sid = input("Enter your student identification number (SID) to start exam: ")
            is_valid_sid = sid.isdigit() and len(sid) == 9
            if is_valid_sid == True:
                pass
            else:
                print("Invalid SID.")
                tries += 1
                continue
            try:
                check_sid_ls(candidates).index(sid)
                break
            except:
                print("Candidate number not found for exam.")
                while True:
                    action = input("Do you want to try again [Y|N]? ")
                    if action.upper() == "Y":
                        break
                    elif action.upper() == "N":
                        break
                    else:
                        print("Response must be [Y|N].")
                if action.upper() == "Y":
                        tries += 1
                        continue
                elif action.upper() == "N":
                        return None
        if tries == 3:
            print("Contact exam administrator.")
        else:
            print("Verifying candidate details...")
            tries = 0
            while tries < 3:
                name = input("Enter your full name as given during registration of exam: ")
                try:
                    assert candidates[check_sid_ls(candidates).index(sid)].name.lower() == name.lower()
                    break
                except:
                    if tries == 2:
                        print("Contact exam administrator to verify documents.")
                        return None
                    print("Name does not match records.")
                    tries += 1
                    continue
            print("Start exam....\n")
            candidates[check_name_ls(candidates).index(name.lower())].do_exam(False)

if __name__ == "__main__":
    main(sys.argv)
