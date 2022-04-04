# Assignment 10

- Username: nheneise
- Commit hash used for grading: b013ee0c299cb449cb1583bd91382341b9cf1b86

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50                  |
| Code Review & style   | 40         |
| Docstrings  | 10                   |


## Total Score: 93/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (43/50 pts)
 
- `sel_sqrt`: 0/4
- `inchtomtuple_lc`: 3/3
- `intomtuple_map`: 3/3

- `bmi_lc`: 3/3
- `bmi_map`: 3/3
- `bmi_cat`: 1/4

- `wbubble_sort`: 15/15
- `rsel_sort`: 15/15



## Code Review & style (40/40 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Problem 1:
    - `sel_sqrt`: 2/2
    - `inchtomtuple_lc`: 5/5
    - `intomtuple_map`: 5/5
    - TA Comments: 

- Problem 2:
    - `bmi_calc`: 3/3
    - `bmi_lc`: 5/5
    - `bmi_map`: 5/5
    - `bmi_cat`: 5/5
    - TA Comments: 

- Problem 3:
    - `wbubble_sort`: 5/5
    - TA Comments: 

- Problem 4:
    - `rsel_sort`: 5/5
    - TA Comments:

- Forbidden functions used (if any): _



## Docstrings and Comments (10/10 pts)
Student's functions all have properly formatted docstrings in the right place. You loose 1-5 point for each function that doesn't have proper docstrings or comment.

- Problem 1: 3/3
- Problem 2: 4/4
- Problem 3: 1/1
- Problem 4: 2/2


TA Comments: 




## Pytest Results
- Test test_sel_sqrt on input (0, 10) should result in [0, 1.0, 4, 1.73, 8, 2.24, 12, 2.65, 16, 3.0, 20]
  but your code gave [0, 1.0, 4, 1.73, 8, 2.24, 12, 2.65, 16, 3.0]
- Test test_sel_sqrt on input (10, 15) should result in [20, 3.32, 24, 3.61, 28, 3.87]
  but your code gave [20, 3.32, 24, 3.61, 28]
- Test test_sel_sqrt on input (15, 20) should result in [3.87, 32, 4.12, 36, 4.36, 40]
  but your code gave [3.87, 32, 4.12, 36, 4.36]
- Test test_sel_sqrt on input (1, 2) should result in [1.0, 4]
  but your code gave [1.0]

- Test test_bmi_cat on input [18.5, 39.22, 19.73, 91.54, 44.1, 41.08, 36.9, 34.06, 16.36, 13.65] should result in [(18.5, 'Normal Weight'), (39.22, 'Obese'), (19.73, 'Normal Weight'), (91.54, 'Obese'), (44.1, 'Obese'), (41.08, 'Obese'), (36.9, 'Obese'), (34.06, 'Obese'), (16.36, 'Underweight'), (13.65, 'Underweight')]
  but your code gave [(18.5, 'Normal'), (39.22, 'Obese'), (19.73, 'Normal'), (91.54, 'Obese'), (44.1, 'Obese'), (41.08, 'Obese'), (36.9, 'Obese'), (34.06, 'Obese'), (16.36, 'Underweight'), (13.65, 'Underweight')]
- Test test_bmi_cat on input [51.01, 81.47, 69.91, 21.87, 57.89, 35.98, 21.96, 30.74, 32.95, 62.68] should result in [(51.01, 'Obese'), (81.47, 'Obese'), (69.91, 'Obese'), (21.87, 'Normal Weight'), (57.89, 'Obese'), (35.98, 'Obese'), (21.96, 'Normal Weight'), (30.74, 'Obese'), (32.95, 'Obese'), (62.68, 'Obese')]
  but your code gave [(51.01, 'Obese'), (81.47, 'Obese'), (69.91, 'Obese'), (21.87, 'Normal'), (57.89, 'Obese'), (35.98, 'Obese'), (21.96, 'Normal'), (30.74, 'Obese'), (32.95, 'Obese'), (62.68, 'Obese')]
- Test test_bmi_cat on input [16.55, 29.01, 25.98, 86.35, 20.4, 9.57, 34.76, 24.4, 66.82, 56.94] should result in [(16.55, 'Underweight'), (29.01, 'Overweight'), (25.98, 'Overweight'), (86.35, 'Obese'), (20.4, 'Normal Weight'), (9.57, 'Underweight'), (34.76, 'Obese'), (24.4, 'Normal Weight'), (66.82, 'Obese'), (56.94, 'Obese')]
  but your code gave [(16.55, 'Underweight'), (29.01, 'Overweight'), (25.98, 'Overweight'), (86.35, 'Obese'), (20.4, 'Normal'), (9.57, 'Underweight'), (34.76, 'Obese'), (24.4, 'Normal'), (66.82, 'Obese'), (56.94, 'Obese')]

