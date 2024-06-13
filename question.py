import random
class Question:
    
    def __init__(self, qtype):
        # you'll need to check if qtype is valid before assigning it
        self.set_type(qtype)
        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None
       
    def set_type(self, qtype):
        """
        Update instance variable qtype.
        """
        if qtype == "end": #check qtype is valid or not
            self.qtype = "end"
            return True
        elif qtype == "single":
            self.qtype = "single"
            return True
        elif qtype == "multiple":
            self.qtype = "multiple"
            return True
        elif qtype == "short":
            self.qtype = "short"
            return True
        else: #if not valid, return False
            self.qtype = None
            return False
    
    def set_description(self, desc):
        """
        Update instance variable description.
        """
        if self.qtype != "end":
            if type(desc) == str and desc != "": #check if desc is a string and isn't empty
                self.description = desc #update instance description
                return True
            else:
                return False
        else:
            return False
        
    def set_correct_answer(self, ans):
        """
        Update instance variable correct_answer.
        """
        if self.qtype != "end":
            if type(ans) == str:
                if self.qtype == "single":
                    try:
                        ["A", "B", "C", "D"].index(ans) # check if ans is in ["A", "B", "C", "D"]
                        self.correct_answer = ans
                        return True
                    except ValueError: # ans is not in ["A", "B", "C", "D"]
                        return False
                elif self.qtype == "multiple":
                    try:
                        ans_Options_List = ans.split(", ") # split ans into a list of answer elements
                        i = 0
                        while i < len(ans_Options_List): # check if each element is in ["A", "B", "C", "D"]
                            ["A", "B", "C", "D"].index(ans_Options_List[i].strip())
                            i += 1
                        self.correct_answer = ans
                        return True
                    except ValueError: # An element is not in ["A", "B", "C", "D"]
                        return False
                elif self.qtype == "short":
                    self.correct_answer = ans
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def set_marks(self, num):
        """
        Update instance variable marks.
        """
        if self.qtype != "end" and (type(num) == int or type(num) == float) and num >= 0:
            self.marks = num
            return True
        else:
            return False
    
    def set_answer_options(self, opts):
        """
        Update instance variable answer_options.

        opts should have all flags equal to False when passed in.
        This method will update the flags based on the correct answer.
        Only then do we check that the number of correct answers is correct.
        """
        opts_List = []
        if self.qtype == "short" or self.qtype == "end":
            self.answer_options = opts
            return True
        else:
            if type(opts) == list:
                i = 0
                while i < len(opts):
                    if (opts[i][0][0:2:] != "A." and
                        opts[i][0][0:2:] != "B." and
                        opts[i][0][0:2:] != "C." and
                        opts[i][0][0:2:] != "D."):
                        return False
                    i += 1
                if len(opts) != 4:
                    return False
                i = 0
                while i < len(opts):
                    if (opts[i][0][0:1:] != ["A", "B", "C", "D"][i]):
                        return False
                    i += 1
                if type(self.correct_answer) != str:
                    return False
                if len(self.correct_answer.split(", ")) != 1 and self.qtype == "single":
                    return False
                elif self.qtype == "multiple" and len(self.correct_answer.split(", ")) < 1:
                    return False
                else:
                    i = 0
                    while i < len(opts):
                        try:
                            self.correct_answer.split(", ").index(opts[i][0][:1:])
                            opts_List.append( (opts[i][0], True) )
                        except ValueError:
                            opts_List.append( (opts[i][0], False) )
                        i += 1
                    self.answer_options = opts_List 
                    return True
            else:
                return False

    def get_answer_option_descriptions(self):
        """
        Returns formatted string listing each answer description on a new line.
        Example:
        A. Answer description
        B. Answer description
        C. Answer description
        D. Answer description
        """
        if self.qtype == "short" or self.qtype == "end" or self.qtype == None:
            return []
        else:
            return f'''{self.answer_options[0][0]}
{self.answer_options[1][0]}
{self.answer_options[2][0]}
{self.answer_options[3][0]}'''

    def mark_response(self, response):
        """
        Check if response matches the expected answer
        Parameter:
            response: str, response provided by candidate
        Returns:
            marks: int|float, marks awarded for the response.
        """
        if self.qtype == "end":
            return None
        elif self.qtype == "multiple":
            list_response = response.strip().split(",")
            list_correct = self.correct_answer.strip().split(",")
            index = 0
            while index < len(list_correct):
                list_correct[index] = list_correct[index].strip()
                index += 1
            i = 0
            marks = 0
            while i < len(list_response):
                try:
                    list_correct.index(list_response[i].strip())
                    marks += self.marks/len(list_correct)
                    i += 1
                except:
                    i += 1
            return round(marks, 2)
        else:
            if response == self.correct_answer: #not completed yet
                return self.marks
            else:
                return 0

    def preview_question(self, i=0, show=True):
        """
        Returns formatted string showing details of question.
        Parameters:
            i: int, placeholder for question number, DEFAULT = 0
            show: bool, True to show Expected Answers, DEFAULT = TRUE
        """
        if i == 0:
            i = "X"
        if self.qtype == "multiple":
            a = "s"
        else:
            a = ""
        if self.qtype == "multiple" or self.qtype == "single":
            if show:
                return f'''Question {i} - {self.qtype.capitalize()} Answer{a}[{self.marks}]
{self.description}
{self.get_answer_option_descriptions()}
Expected Answer: {str(self.correct_answer)}'''
            else:
                return f'''Question {i} - {self.qtype.capitalize()} Answer{a}[{self.marks}]
{self.description}
{self.get_answer_option_descriptions()}
Response for Question {i}: '''
        elif self.qtype == "short":
            if show:
                return f'''Question {i} - {self.qtype.capitalize()} Answer[{self.marks}]
{self.description}
Expected Answer: {str(self.correct_answer)}'''
            else:
                return f'''Question {i} - {self.qtype.capitalize()} Answer[{self.marks}]
{self.description}
Response for Question {i}: '''
        elif self.qtype == "end":
            return '''-End-'''
    @staticmethod
    def generate_order():
        """
        Returns a list of 4 integers between 0 and 3 inclusive to determine order.

        Sample usage:
        >>> generate_order()
            [3,1,0,2]
        """
        order = []
        while len(order) < 4:
            a = random.randint(1, 4)
            try: 
                order.index(a)
            except ValueError:
                order.append(a)
        return order

    def shuffle_answers(self):
        """
        Updates answer options with shuffled elements.
        Must call generate_order only once.
        """
        order = self.generate_order()
        i = 0
        new_Opts = []
        new_correct = []
        letters = ["A", "B", "C", "D"]
        while i < 4:
            new = (letters[i]+self.answer_options[order[i]][0][1:], self.answer_options[order[i]][1])
            new_Opts.append(new)
            if new[1] == True:
                new_correct.append(new[0][0])
            i += 1
        self.answer_options = new_Opts
        i = 0
        string = ""
        while i < len(new_correct):
            string += new_correct[i]
            if i < len(new_correct) - 1:
                string += ", "
            i += 1
        self.correct_answer = string
    
    def copy_question(self):
        new_question = Question(self.qtype)
        new_question.set_description(self.description)
        new_question.set_correct_answer(self.correct_answer)
        new_question.set_answer_options(self.answer_options)
        new_question.set_marks(self.marks)
        return new_question

    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''
        return f'''Question {self.__hash__()}:
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''

