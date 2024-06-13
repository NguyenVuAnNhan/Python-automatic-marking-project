# Test Case Designs
Complete the given tables with details of your test case design for each question type.
State the values to initalize appropriate `Question` objects required for the test case.

Question 1:
    Type: short
    Description: "What's the capital of Vietnam"
    Correct Answer: "Hanoi"
    Marks: 5

Question 2:
    Type: single
    Description: "What's the correct answer"
    Correct Answer: A
    Answer options: "A. the correct answer", "B. I don't know", "C. I'm not sure", "D. I gave up"
    Marks: 2

Question 3:
    Type: multiple
    Description: "What's the correct answer"
    Correct Answer: A, B
    Answer options: "A. the correct answer", "B. the other correct answer", "C. I'm not sure", "D. I gave up"
    Marks: 2

Column descriptions:
* Test ID - Test case identification number
* Description - Type of testcase and brief explanation of test case details
* Inputs - Arguments into the method
* Expected Output - Return values of the method
* Status - pass/fail 

Table 1: Summary of test cases for method `mark_response` for question type `short`

| Test ID |     Description            |    Inputs      | Expected Output  | Status |
| ------- | -------------------------- | -------------- | ---------------- | ------ |
|    1    | Positive: right response   | "Hanoi"        |        5         | Passed |
|    2    | Negative: wrong response   | "Walter"       |        0         | Passed |
|    3    | Negative: empty string     | ""             |        0         | Passed |

Table 2: Summary of test cases for method `mark_response` for question type `single`

| Test ID |     Description            |    Inputs      | Expected Output  | Status |
| ------- | -------------------------- | -------------- | ---------------- | ------ |
|    1    | Positive: right response   | "A"            |        2         | Passed |
|    2    | Negative: wrong response   | "C"            |        0         | Passed |
|    3    | Negative: empty string     | ""             |        0         | Passed |
|    4    | Negative: > 1 option       | "A, D"         |        0         | Passed |

Table 3: Summary of test cases for method `mark_response` for question type `multiple`

| Test ID |     Description            |    Inputs      | Expected Output  | Status |
| ------- | -------------------------- | -------------- | ---------------- | ------ |
|    1    | Positive: right response   | "A, B"         |        2         | Passed |
|    2    | Negative: wrong response   | "C, D"         |        0         | Passed |
|    3    | Negative: empty string     | ""             |        0         | Passed |
|    4    | Negative: 1 right option   | "A, D"         |        1         | Passed |
|    5    | Negative: 1 right option   | "A"            |        1         | Passed |

# 
