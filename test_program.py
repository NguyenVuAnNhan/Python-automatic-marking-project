'''
Write instructions to execute your test program here.
'''
import question
'''
Nhan Nguyen Vu An - 530604594 - Testing module

Instructions:

There are 12 test cases, each would correspond to a specific situation
that the mark_response() method must handle.

Every test case will include a summary, the input, expected output, actual
output and overall conclusion (Passed/Failed).

There is a test all test cases functionality at the bottom of this program.
It will show whether the method pass all test cases or not.

To run the tests, simply run this program.
'''


#Test Case Design:

#Initialise question 1 - Short:
q1 = question.Question("short")
desc = "What's the capital of Vietnam"
correct = "Hanoi"
mark = 5

q1.set_description(desc)
q1.set_correct_answer(correct)
q1.set_marks(mark)

#Initialise question 2 - Single:
q2 = question.Question("single")
desc = "What's the correct answer"
correct = "A"
options = ["A. the correct answer", "B. I don't know", "C. I'm not sure", "D. I gave up"]
mark = 2

q2.set_description(desc)
q2.set_correct_answer(correct)
q2.set_answer_options(options)
q2.set_marks(mark)

#Initialise question 3 - Multiple:
q3 = question.Question("multiple")
desc = "What's the correct answer"
correct = "A, B"
options = ["A. the correct answer", "B. the other correct answer", "C. I'm not sure", "D. I gave up"]
mark = 2

q3.set_description(desc)
q3.set_correct_answer(correct)
q3.set_answer_options(options)
q3.set_marks(mark)

#Test cases:
# Test cases for Short
def test_1():
    expected = 5
    result = q1.mark_response("Hanoi")
    assert result == expected, "Test_1 failed"
    return True

def test_2():
    expected = 0
    result = q1.mark_response("Walter")
    assert result == expected, "Test_2 failed"
    return True

def test_3():
    expected = 0
    result = q1.mark_response("")
    assert result == expected, "Test_3 failed"
    return True

# Test cases for Single
def test_4():
    expected = 2
    result = q2.mark_response("A")
    assert result == expected, "Test_4 failed"
    return True

def test_5():
    expected = 0
    result = q2.mark_response("C")
    assert result == expected, "Test_5 failed"
    return True

def test_6():
    expected = 0
    result = q2.mark_response("")
    assert result == expected, "Test_6 failed"
    return True

def test_7():
    expected = 0
    result = q2.mark_response("A, D")
    assert result == expected, "Test_7 failed"
    return True

# Test cases for Multiple
def test_8():
    expected = 2
    result = q3.mark_response("A, B")
    assert result == expected, "Test_8 failed"
    return True

def test_9():
    expected = 0
    result = q3.mark_response("C, D")
    assert result == expected, "Test_9 failed"
    return True

def test_10():
    expected = 0
    result = q3.mark_response("")
    assert result == expected, "Test_10 failed"
    return True

def test_11():
    expected = 1
    result = q3.mark_response("A, D")
    assert result == expected, "Test_11 failed"
    return True

def test_12():
    expected = 1
    result = q3.mark_response("A")
    assert result == expected, "Test_12 failed"
    return True


if test_1():
    print("Test_1 is successful")
if test_2():
    print("Test_2 is successful")
if test_3():
    print("Test_3 is successful")

if (test_1() and test_2() and test_3()):
    print("All Short test cases ran successfully")

if test_4():
    print("Test_4 is successful")
if test_5():
    print("Test_5 is successful")
if test_6():
    print("Test_6 is successful")
if test_7():
    print("Test_7 is successful")

if (test_4() and test_5() and test_6() and test_7()):
    print("All Single test cases ran successfully")

if test_8():
    print("Test_8 is successful")
if test_9():
    print("Test_9 is successful")
if test_10():
    print("Test_10 is successful")
if test_11():
    print("Test_11 is successful")
if test_12():
    print("Test_12 is successful")

if (test_8() and test_9() and test_10() and test_11() and test_12()):
    print("All Multiple test cases ran successfully")

if (test_1() and test_2() and test_3())\
    and (test_4() and test_5() and test_6() and test_7())\
    and (test_8() and test_9() and test_10() and test_11() and test_12()):
    print("All test cases ran successfully")

