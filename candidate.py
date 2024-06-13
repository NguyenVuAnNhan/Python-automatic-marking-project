import os
class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        '''
        Returns total duration of exam.
        '''
        return (self.extra_time + self.exam.duration)
            
    def edit_sid(self, sid):
        '''
        Update attribute sid
        '''
        if type(sid) == str and len(sid) == 9 and int(sid) > 0:
            self.sid = sid

    def edit_extra_time(self, t):
        '''
        Update attribute extra_time
        '''
        if type(t) == int and t >= 0:
            self.extra_time = t
    
    def set_confirm_details(self, sid, name):
        '''
        Update attribute confim_details
        '''
        if self.sid == str(sid) and self.name == str(name):
            self.confirm_details = True
            return True
        else:
            return False

    def log_attempt(self, data):
        '''
        Save data into candidate's file in Submissions.
        '''
        path = self.exam.path_to_dir + f"/submissions/{self.sid}.txt"
        try:
            fobj = open(path, "w")
        except:
            os.mkdir(self.exam.path_to_dir + "/submissions")
            fobj = open(path, "w")
        fobj.write(data)
        fobj.close()
        
    
    def set_results(self, ls):
        '''
        Update attribute results if confirm_details are True
        '''
        if self.confirm_details and len(ls) == (len(self.exam.questions) - 1):
            self.results = ls

    def do_exam(self, preview = True):
        '''
        Display exam and get candidate response from terminal during the exam.
        '''
        if preview == True:
            print(f'''Candidate: {self.name}({self.sid})
Exam duration: {self.get_duration()} minutes
You have {self.get_duration()} minutes to complete the exam.
{self.exam.preview_exam(False)}'''[:-2:])
        else:
            print(f'''Candidate: {self.name}({self.sid})
Exam duration: {self.get_duration()} minutes
You have {self.get_duration()} minutes to complete the exam.\n{self.exam.get_name()}''')
            index = 0
            data = ''
            while index < len(self.exam.questions):
                string = f"{self.exam.questions[index].preview_question(index+1, False)}"
                print(string, end = "")
                data += string
                if self.exam.questions[index].qtype != "end":
                    ans = input()
                    marks = self.exam.questions[index].mark_response(ans)
                    data += (ans + f'''\nYou have scored {'{0:.2f}'.format(marks)} marks.\n\n''')
                print()
                index += 1
            data += "\n"
            self.log_attempt(data)


    def __str__(self):
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.get_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam(False)
        str_out = name + duration + exam
        return str_out

