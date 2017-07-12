"""
 SOLUTION FOR THE PROJECT SUDOKU SOLVER OF THE AIND
"""


def sudoku_descriptors():
    # Create boxes, units, peers and diagonals
    rows = 'ABCDEFGHI'
    cols = '123456789'
    
    boxes = cross(rows, cols)

    row_units = [cross(r, cols) for r in rows]
    col_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs)
                    for rs in chunks(rows, 3)
                    for cs in chunks(cols, 3)]

    unitlist = row_units + col_units + square_units
    main_diagonal = [rows[index] + cols[index]
                     for index in range(0, len(rows))]
    second_diagonal = [rows[len(rows) - 1 - index] + cols[index] 
                       for index in range(0, len(rows))]

    unitlist.append(main_diagonal)
    unitlist.append(second_diagonal)

    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)

    return (
        rows,
        cols,
        unitlist,
        boxes,
        units,
        peers,
        main_diagonal,
        second_diagonal
    )

def cross(A, B):
    """Cross product of elements in A and elements in B."""
    return [s + t for s in A for t in B]


def chunks(l, n):
    """Creates chunks of size n of an array l"""
    return [l[i:i + n] for i in range(0, len(l), n)]


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def grid_values(grid, wild_card='.'):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    assert len(grid) == 81, "The length of `grid` should be 81. A 9x9 sudoku."
    sudoku_dict = {}
    for index, letter in enumerate(grid):
        sudoku_dict[boxes[index]] = letter if letter != wild_card else '123456789'
    return sudoku_dict


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    print('\n')
    return


def eliminate(values):
    for box, value in values.items():
        if len(value) == 1:
            for peer in peers[box]:
                values[peer] = values[peer].replace(value, '')
    return values


def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    count = 0
    stalled = False
    while max(len(values[s]) for s in boxes) > 1 and not stalled:
        initial_state = values.copy()
        values = eliminate(values)
        values = only_choice(values)
        count += 1
        stalled = initial_state == values
        if min(len(values[s]) for s in boxes) == 0:
            return False
    return values


def search(sudoku_0):
    # Using depth-first search and propagation, create a search tree and solve the sudoku."

    # First, reduce the puzzle using the previous function
    sudoku_0 = reduce_puzzle(sudoku_0)
    if not sudoku_0:
        return False
    if sudoku_is_solved(sudoku_0):
        return sudoku_0

    # Choose one of the unfilled squares with the fewest possibilities
    chosen_box = find_better_box(sudoku_0)

    # Now use recursion to solve each one of the resulting sudokus,
    # and if one returns a value (not False), return that answer!
    for value in sudoku_0[chosen_box]:
        sudoku_1 = sudoku_0.copy()
        sudoku_1[chosen_box] = value
        sudoku_2 = search(sudoku_1)
        if sudoku_2:
            return sudoku_2


def sudoku_is_solved(sudoku_dict):
    len_boxes = [len(sudoku_dict[s]) for s in boxes]
    return min(len_boxes) == 1 and max(len_boxes) == 1


def find_better_box(sudoku_dict):
    len_boxes = [s for s in boxes if len(sudoku_dict[s]) > 1]
    min_length = min(len(sudoku_dict[s]) for s in len_boxes)
    min_len_box = [s for s in len_boxes if len(sudoku_dict[s]) == min_length]
    return min_len_box[0]


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in unitlist:
        twin_candidates = [box for box in unit if len(values[box]) == 2]
        twins = [a for i, a in enumerate(twin_candidates) for j, b in enumerate(twin_candidates) if values[a] == values[b] and i != j]
        for twin in twins:
            value = values[twin]
            for box in unit:
                if values[box] != value:
                    for digit in value:
                        values[box] = values[box].replace(digit, '')
    return values


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(naked_twins(grid_values(grid)))


assignments = []
rows, cols, unitlist, boxes, units, peers, main_diagonal, second_diagonal = sudoku_descriptors()

if __name__ == '__main__':
    
    # Evaluate the grid
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. \
               Not a problem! It is not a requirement.')
