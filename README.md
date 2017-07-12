# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We use constraint propagation in this case in order to reduce the number of solutions in each iteration or propagation, for reaching the point where we can detect the twins. Each constraint limits our solution space, and propagating these contraints one after each other iteratively helps us reduce the number of possible values. Without these previous propagation we wouldn't reach a point where the values are pairs to match the twins. And finally, the naked twins approach allows us to add one more contraint to our model, reducing our solution space even more to solve it.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: To solve the diagonal sudoku problem, we are adding a new constraint to our model, that are the diagonals rule of non-repeated numbers. Previously the constraints were only for columns, rows, and 3x3 squares. Now with this aditional constraint the propagation is done taking into consideration one more rule that has to consider before the reduction of the possible values for each box.

## How to use

Having a Sudoku like this:
```
. . . |. . . |8 . 6
8 . . |. . . |. . .
. 7 . |. 8 6 |3 . .
------+------+------
. . . |8 . . |. . .
. . . |. . . |. 8 .
. 8 . |5 . 9 |. . .
------+------+------
1 . 8 |. . . |. . .
. . . |. . . |. . 8
. . . |. . 8 |. 4 .
```
It should be written in a one-line string, and the function `solve()` can be used, and the response is a dictionary containing the key and value for every box of the sudoku. To print the solution you can use the `display()` function:
```
from solution import solve, display

sudoku_grid = '......8.68.........7..863.....8............8..8.5.9...1.8..............8.....8.4.'
sudoku_solved = solve(sudoku_grid)
display(sudoku_solved)

# Result
2 3 4 |7 9 5 |8 1 6
8 5 6 |1 3 2 |4 9 7
9 7 1 |4 8 6 |3 2 5
------+------+------
3 9 2 |8 7 1 |5 6 4
5 1 7 |6 4 3 |9 8 2
4 8 2 |5 6 9 |7 3 1
------+------+------
1 4 8 |3 2 7 |6 5 9
3 2 9 |6 5 4 |1 7 8
7 6 5 |9 1 8 |2 4 3
```

## Project Details

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

