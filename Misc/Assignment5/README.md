# Assignment5

Username: nheneise
Commit hash used for grading: 87f6d4a1d7de8279daecfc5c85800ea6228f9b74

Rubric (see Canvas page):

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests   | 50           |
| Docstrings and Comments  | 20           |
| Code Review & style   | 30           |

## Total Score: 90.5/100
Please double-check that your Canvas score reflects what is shown here.

Your total score should be subtraction of violation points(see TA Comments in Code Review & style  ) from sum of the sections.


## Code Tests (42/50 pts)

- `log_2`: 1/1
- `makeProbability`: 3/3
- `entropy`: 1/3
- `magick`: 4/4
- `is_magic_square`: 4/4
- `generate_3_square`: 3/3
- `encrypt`: 2/3
- `decrypt`: 2/3
- `encrypt_sentence`: 1/3
- `decrypt_sentence`: 1/3
- `make_number`: 2/2
- `convert`: 2/2
- `mul_`: 3/3
- `add_`: 3/3
- `get_amino_acids`: 3/3
- `get_DNA`: 3/3
- `translate`: 4/4

## Docstrings and Comments (18.5/20 pts)

- Student's functions all have properly formatted docstrings in the right place: 15.5/17 pts

Note: -0.5 for each missing or obviously incomplete docstring.

- Student uses inline comments to explain major blocks, if necessary: 3/3 pts


TA Comments: Missing the last three docstrings


## Code Review & style (30/30 pts)
Your code is reviewed for proper style and legibility.
If your code passes the autograder, but you violated the specifications (for example using forbidden python features/functions), you will lose the autograder points as well!

- Code Review `Problem 1`: 3/3
- Code Review `Problem 2`: 3/3
- Code Review `Problem 3`: 6/6
- Code Review `Problem 4`: 6/6
- Code Review `Problem 5`: 6/6
- Code Review `Problem 6`: 6/6

TA Comments: 

- The violations (If any): _
- Subtractions from code test section (If any): _



## Pytest Results
- Expected entropy on input [0.375, 0.433, 0.192] to return 1.51
- Expected entropy on input [0.001, 0.999] to return 0.01


- Expected encrypt on input ('z', 5) to return 'd'

- Expected decrypt on input ('d', 5) to return 'z'

- Expected encrypt_sentence on input ('two roads diverged in a green wood', 2) to return 'vyqbtqcfubfkxgtigfbkpbcbitggpbyqqf'
- Expected encrypt_sentence on input ('the quick brown fox jumps over the lazy dog', 10) to return 'croj{dsmujlayfxjpygjtdwzbjyeoajcrojvkihjnyq'

- Expected decrypt_sentence on input ('vyqbtqcfubfkxgtigfbkpbcbitggpbyqqf', 2) to return 'two roads diverged in a green wood'
- Expected decrypt_sentence on input ('croj{dsmujlayfxjpygjtdwzbjyeoajcrojvkihjnyq', 10) to return 'the quick brown fox jumps over the lazy dog'


