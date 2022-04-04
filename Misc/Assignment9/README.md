# Assignment 9

- Username: nheneise
- Commit hash used for grading: d4cb48c1c6351fe0a32f40f6986b2cd09b74ccac

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50                  |
| Docstrings  | 15                   |
| Code Review & style   | 20         |
| Student Tests | 15                 |  


## Total Score: 70/100
Please double-check that your Canvas score reflects what is shown here. 



## Code Tests (40/50 pts)
 
- `pop`: 2/2
- `error`: 5/6


- `get_dic`: 5/5
- `get_state_pop`: 5/5
- `scd`: 4/4
- `ccc`: 5/6
- `sdd`: 0/5
- `usdd`: 5/5


- `simpson`: 9.6/12


## Docstrings and Comments (10/15 pts)
Student's functions all have properly formatted docstrings in the right place. You loose 1,5 point for each function that doesn't have proper docstrings or comment.

- Problem 1: 3/3
- Problem 2: 5/10
- Problem 3: 2/2


TA Comments: None od the docstrings tell us what is being returned in the out. The type of the output is mentioned but now hat it is ? for example, for ccc function, you can say that out (int): Number of confirmed cases. This is true for other docstrings too. 



## Code Review & style (20/20 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `pop`: 2/2
    - `error`: 2/2
    - TA Comments: 

- Problem 2:
    - `scd`: 2/2
    - `ccc`: 2/2
    - `sdd`: 2/2
    - `usdd`: 2/2
    - `get_dic`: 2/2
    - `get_state_pop`: 2/2
    - TA Comments: 

- Problem 3:
    - `simpson`: 4/4
    - TA Comments: 


- Forbidden functions used (if any): _


## Student Tests (0/15 pts)
We check that you added reasonably comprehensive test cases to your `test_a9.py` file. 

- `test_pop`: 0/4
- `test_error`: 0/4
- `test_get_data`: 0/3
- `test_simpson`: 0/4

- TA Comments: No Student tests provided.

## Pytest Results
- Test test_error threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 29, in test_error
    yield x, y, (a9.error(x)), (round(a9.error(x), 2) == round(y, 2))
  File "./a9.py", line 53, in error
    errorList.append([abs((data[i][1])-graph[i][1])/data[i][1]])
IndexError: list index out of range



- Test test_ccc threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 90, in test_ccc
    y_produced = a9.ccc(test_dic, x)[y]
KeyError: (100000, 120000)



- Test test_simpson threw error:
Traceback (most recent call last):
  File "a9_RunAutograder.py", line 126, in <module>
    for x, y, y_actual, result in f():
  File "./a9_grader.py", line 131, in test_simpson
    yield x, z, (a9.simpson(*y)), (approx(a9.simpson(*y)) == z)
  File "./a9.py", line 321, in simpson
    for i in range(a - zero, n + 1):
TypeError: 'float' object cannot be interpreted as an integer



