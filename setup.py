'''
Functions to setup the exam questions and candidate list for the exam.
'''
# please do not change or add another import
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each question found in the file.
    General procedure to extract question.
    1. Extract the following
        - type
        - question details (description)
        - possible answers (if any)
        - expected answer
        - marks
        (you shouldn't need to perform error handling on these details,
        this is handled in the next step).
    2. You'll need to convert the possible answers (if any) to a list of tuples (see 
       "Section 1. Setup the exam - Question" for more details). All flags can be False.
    3. Create a question object and call the instance methods to set the
       attributes. This will handle the error handling.
    4. Repeat Steps 1-3 for the next question until there are no more questions.
    5. You will need to create an end question as well.
    6. Create the list for all your questions and return it.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Question objects.
    """
    def line_reader(a_question):
        lines = a_question.split("\n")
        index = 0 
        flag = True
        while index < len(lines):
            if lines[index].startswith("Question - "):
                inquiry = question.Question(lines[index].split("- ")[1].rstrip().lower())
            if inquiry.qtype == "single" or inquiry.qtype == "multiple":
                if lines[index].startswith("Possible Answers:"):
                    desc = []
                    new_index = 1
                    while new_index < index:
                        desc.append(lines[new_index])
                        new_index += 1
                    description = "\n".join(desc)
                    inquiry.set_description(description)
                    options_ls = []
                    while not lines[index + 1].startswith("Expected Answer:"):
                            options_ls.append((lines[index + 1], False))
                            index += 1
                if lines[index].startswith("Expected Answer: "):
                    correct = lines[index].split(":")[1].rstrip()[1::]
                    inquiry.set_correct_answer(correct)
                    inquiry.set_answer_options(options_ls)
            else:
                if (lines[index].startswith("Possible Answers:") or lines[index].startswith("Expected Answer:")) and flag:
                    desc = []
                    new_index = 1
                    while new_index < index:
                        desc.append(lines[new_index])
                        new_index += 1
                    description = "\n".join(desc)
                    inquiry.set_description(description)
                    correct = lines[index].split(":")[1].rstrip()[1::]
                    inquiry.set_correct_answer(correct)
                    flag = False
            if lines[index].startswith("Possible Answers:"):
                    desc = []
                    new_index = 1
                    while new_index < index:
                        desc.append(lines[new_index])
                        new_index += 1
                    description = "\n".join(desc)
                    options_ls = []
                    while not lines[index + 1].startswith("Expected Answer:"):
                            options_ls.append((lines[index + 1], False))
                            index += 1
                    inquiry.set_answer_options(options_ls)
            if lines[index].startswith("Expected Answer: "):
                    correct = lines[index].split(":")[1].rstrip()[1::]
                    inquiry.set_correct_answer(correct)
            if lines[index].startswith("Marks: "):
                marks = int(lines[index].split(":")[1].rstrip())
                inquiry.set_marks(marks)
            index += 1
        return inquiry

    questions = fobj.read().split("\n\n") # Split file into questions

    i = 0
    question_list = []

    while i < len(questions):
        question_list.append(line_reader(questions[i]))
        i += 1
    question_list.append(question.Question("end"))

    return question_list

def sort(to_sort: list, order: int=0)->list:
    """
    Sorts to_sort depending on settings of order.

    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.

    Sample usage:
    >>> to_sort = [(1.50, "orange"), (1.02, "apples"), (10.40, "strawberries")]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: [(1.5, 'orange'), (1.02, 'apples'), (10.4, 'strawberries')]
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: [(1.02, 'apples'), (1.5, 'orange'), (10.4, 'strawberries')]
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: [(10.4, 'strawberries'), (1.5, 'orange'), (1.02, 'apples')]
    >>> to_sort = [ "oranges", "apples", "strawberries"]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: ['oranges', 'apples', 'strawberries']
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: ['apples', 'oranges', 'strawberries']
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: ['strawberries', 'oranges', 'apples']
    """
    if order == 0 or order > 2:
        ls = to_sort
        return ls
    elif order == 1:
        ls = to_sort
        index = 0
        while index < len(ls)^2:
            i = 0
            while i < (len(ls) - 1):
                if ls[i][0] > ls[i+1][0]:
                    new = ls[i]
                    ls[i] = ls[i+1]
                    ls[i+1] = new
                i += 1
            index += 1
        return ls
    elif order == 2:
        ls = to_sort
        index = 0
        while index < len(ls)^2:
            i = 0
            while i < (len(ls) - 1):
                if ls[i][0] < ls[i+1][0]:
                    new = ls[i]
                    ls[i] = ls[i+1]
                    ls[i+1] = new
                i += 1
            index += 1
        return ls
    else:
        return []


def extract_students(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    try:
        a = fobj.read().split("\n")
    except:
        return []
    ls = []
    array = []
    index = 0
    while index < len(a):
        array.append(a[index].split((",")))
        index += 1
    index = 1
    while index < len(a) - 1:
        if array[index][2] == "":
            array[index][2] = 0
        ls.append((array[index][0], array[index][1], int(array[index][2])))
        index += 1
    ls = sort(ls,1)
    ls_cand = []
    index = 0
    while index < len(ls):
        cand = candidate.Candidate(ls[index][0], ls[index][1], int(ls[index][2]))
        ls_cand.append(cand)
        index += 1
    return ls_cand

