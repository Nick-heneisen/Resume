# Assignment4

Username: nheneise
Commit hash used for grading: 5b17f1ef9fcc6bb060b2edb4e64f7087dedffec6

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Passes Tests    | 40           |
| Code Review   | 40           |
| Docstrings and Comments   | 20         |

## Lab Checkoff
There was no assignment credit for lab checkoff this week.

## Total Score: 75/100
Please double-check that your Canvas score reflects what is shown here.

## Code Tests (25/40 pts)
- `block`: 1/1
- `square`: 2/2
- `purchase`: 2/2
- `how_much`: 1/1
- `find_num_min`: 2/2
- `search_me_me_bee`: 1/1
- `search_go_to_out`: 2/2
- `increase`: 2/2
- `letter_count`: 2/2
- `dot_prod`: 1/1
- `scalar_vec`: 1/1
- `euc_len`: 1/1
- `ang_vec`: 1/1
- `unit_vec`: 1/1
- `vec_op`: 2/2
- `tree_age`: 1/1
- `noninvasive_tree_age`: 1/1
- `make_unique`: 0/1
- `partition`: 0/2
- `occurs_at_index`: 0/1
- `intersect`: 0/1
- `optimum`: 0/2
- `sigma`: 0/1
- `sigma_square`: 0/1
- `sigma_product`: 0/1
- `separate`: 0/1
- `linear_model`: 1/1
- `make_linear`: 0/1
- `reverse`: 0/1
- `palindrome`: 0/2

## Code Review (30/40 pts)
Your code is reviewed for proper style.  For each problem, the TA who grades you will verify that you
- did not use functions or types that shortcut the work (e.g. `set` for `make_unique`)
- wrote legible code
- put your test code in `if __name__ == "__main__"` or in a pytest file

Breakdown:
- `Problem 1`: 3/4
- `Problem 2`: 4/4
- `Problem 3`: 4/4
- `Problem 4`: 4/4
- `Problem 5`: 4/4
- `Problem 6`: 4/4
- `Problem 7`: 4/4
- `Problem 8`: 3/3
- `Problem 9`: 0/3
- `Problem 10`: 0/3
- `Problem 11`: 0/3

TA Comments: 

## Part 1 Docstrings and Comments (20/20 pts)
- Student's functions all have properly formatted docstrings: 5/15 pts

Note: -0.5 for each missing or obviously incomplete docstring.

- Student uses inline comments to explain major blocks, if necessary: 5/5 pts

TA Comments: 

## Pytest Results
Function make_unique threw error: 'NoneType' object is not iterable

Function partition threw error: 'NoneType' object is not iterable

Function occurs_at_index threw error: 'NoneType' object is not iterable

Function intersect threw error: 'NoneType' object is not iterable

Expected optimum(([1, 1, -1, 100, -100], 0)) ==> -100
Expected optimum(([1, 1, -1, 100, -100], 1)) ==> 100

Expected sigma([100, 10, 1]) ==> 111

Expected sigma_square([10, 2, 3]) ==> 113

Expected sigma_product(([1, 2, 3], [1, 10, 100])) ==> 321

Expected separate([[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]) ==> [[1, 2, 4, 3, 5], [1, 3, 3, 2, 5]]

Function make_linear threw error: 'NoneType' object is not subscriptable

Expected reverse(abc) ==> cba

Expected palindrome(Was it a cat I saw?) ==> True
Expected palindrome(Oreos yum!) ==> False

