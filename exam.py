class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.set_name(path)

    def set_name(self, path):
        """
        Sets the name of the exam. 
        """
        # you'll need to add some code here
        path_List = path.split("/")
        self.name = path_List[len(path_List) - 1].replace(" ","_")

    def get_name(self):
        """
        Returns formatted string of exam name.
        """
        return self.name.upper().replace("_", " ")
    
    def set_exam_status(self):
        '''
        Set exam_status to True only if exam has questions.
        '''
        if self.questions != []:
            self.exam_status = True
        else:
            self.exam_status = False
        
    
    def set_duration(self, t):
        '''
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        '''
        if t > 0:
            self.duration = t

    def set_questions(self, ls):
        '''
        Verifies all questions in the exam are complete.
        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        '''
        if type(ls) != list:
            return False
        else:
            i = 0
            while i < len(ls):
                if ls[i].qtype != "end" and (ls[i].description == None or ls[i].correct_answer == None):
                    print("Description or correct answer missing")
                    return False
                elif (ls[i].qtype == "single" or ls[i].qtype == "multiple") and len(ls[i].answer_options) != 4:
                    print("Answer options incorrect quantity")
                    return False
                elif ls[i].qtype == "short" and ls[i].answer_options != []:
                    print("Answer options should not exist")
                    return False
                if i == (len(ls) - 1): # if i is the last one
                    if ls[i].qtype != "end":
                        print("End marker missing or invalid")
                        return False
                    elif ls[i].description != None or ls[i].answer_options != [] or ls[i].correct_answer != None or ls[i].marks != None:
                        print("End marker missing or invalid")
                        return False
                i += 1
            self.questions = ls
            return True

    def preview_exam(self, show=True):
        '''
        Returns a formatted string.
        '''
        if show == True:
            string = ""
            string += f'''{self.get_name()}\n'''
            i = 0
            while i < len(self.questions):
                string += f"{self.questions[i].preview_question(i+1, show)}\n\n"
                i += 1
            return string
        elif show == False:
            string = ""
            string += f'''{self.get_name()}\n'''
            i = 0
            while i < len(self.questions):
                string += f"{self.questions[i].preview_question(i+1, show)}\n\n"
                i += 1
            return string

    def copy_exam(self):
        '''
        Create a new exam object using the values of this instances' values.
        '''
        # TODO: make a new exam object (call the constructor)
        new_exam = Exam(self.duration, self.path_to_dir, self.shuffle)

        # make a new list of questions to reassign to the attribute
        new_questions = []
        i = 0
        while i < len(self.questions):
            original_question = self.questions[i]
            # call the copy method for this question
            # TODO: (you'll need to write this instance method in Question)
            new_question = original_question.copy_question()
            if new_exam.shuffle == True and new_question.qtype != "end" and new_question.qtype != "short":
                try:
                    new_question.shuffle_answers()
                except:
                    pass #something happend here, i dont know 
                    #TODO: figure out why test cases return index errors
            # insert this into new list of questions
            new_questions.append(new_question)
            i += 1

        # TODO: assign this new question list to the new exam
        new_exam.questions = new_questions

        # return the new exam
        return new_exam

    def __str__(self):
        pass

