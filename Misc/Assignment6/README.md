# Assignment6

Username: nheneise
Commit hash used for grading: eb09521f221c20bd69f7fcdd9c861b28d5aada68

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests (Part 1: Decode)   | 25           |
| Code Tests (Part 2: Grey Scale) | 25   |
| Docstrings  | 15           |
| Code Review & style   | 20           |
| Student Tests | 15    |

## Total Score: 88/100
Please double-check that your Canvas score reflects what is shown here.


## Code Tests (Part 1: Decode) (18/25 pts)

- Successfully writes to file: 6/6
- Written file has correct ppm format: 6/6
- `process_ppm` writes the correct contents to file: 6/6
- `color_translate` returns the correct string: 0/7


## Code Tests (Part 2: Grey Scale) (15/25 pts)

- Successfully writes to file: 6/6
- Written file has correct ppm format: 6/6
- Values in written file are within 0 and 255: 3/3
- `grey_scale` returns the correct string: 0/10


## Docstrings and Comments (15/15 pts)
Student's functions all have properly formatted docstrings in the right place
- `color_translate`: 5/5
- `process_ppm`: 5/5
- `grey_scale` : 5/5

TA Comments: 


## Code Review & style (20/20 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!
- `color_translate`: 4/4
- `process_ppm`: 4/4
- `main_part1` : 4/4
- `grey_scale` : 4/4
- `main` : 4/4

TA Comments: 

- Forbidden functions used (if any): _


## Student Tests (20/20 pts)
We check that you added reasonably comprehensive test cases to your `test_process_ppm.py` file.
- `color_translate`: 10/10
- `grey_scale` : 10/10

## Pytest Results
- Test test_color_translate on input '0 0 0 0 0 0' should result in '  0   0   0   0   0   0'
  but your code gave ' \n 0 \n \n 0 \n \n 0 \n \n 0 \n '
- Test test_color_translate on input '1 2 3 4 5 6' should result in '153 255   0 153 255   0'
  but your code gave ' \n 0 \n \n 153 \n \n 255 \n \n 0 \n '
- Test test_color_translate on input '10 20 30 40 50 60 70 80 90' should result in '153 255   0 153 255   0 153 255   0'
  but your code gave ' 255 \n 0 \n \n 0 \n 0 \n \n 153 \n 0 \n \n 255 \n 0 \n \n 0 \n 0 \n \n 153 \n 0 \n \n 255 \n 0 \n \n 0 \n 0 \n '
- Test test_color_translate on input '153 0 255 255 153 0' should result in '  0   0   0   0   0   0'
  but your code gave ' \n 0 \n \n 255 \n 255 \n 255 \n \n 255 \n 255 \n 255 \n \n 153 \n 255 \n 0 \n \n 0 \n '

- Test test_grey_scale threw error:
Traceback (most recent call last):
  File "2.5-RunAutograder.py", line 179, in <module>
    for x, y, y_actual, result in f():
  File "./a6_grader.py", line 307, in test_grey_scale
    y_actual = ppm_modify.grey_scale(x)
  File "./ppm_modify.py", line 128, in grey_scale
    grey = int(sqrt(int(i[j]) + int(i[j - 1]) + int(i[j - 2])))
IndexError: list index out of range



