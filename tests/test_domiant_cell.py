from src.domiant_cell import solve

def test_solve_1x2():
    grid = [
        [1, 2]
    ]
    assert 1 == solve(grid)

def test_solve_2x1():
    grid = [
        [ 1 ],
        [ 2 ]
    ]
    assert 1 == solve(grid)

def test_solve_1x2():
    grid = [
        [1, 1]
    ]
    assert 0 == solve(grid)


def test_solve_base():
    grid = [
        [1, 2, 7],
        [4, 5, 6],
        [8, 8, 9],
    ]

    "7 and 9 are domiant cell"
    assert 2 == solve(grid)

def test_solve_4x4():
    grid = [
        [0, 1, 1, 1],
        [1, 2, 1, 1],
        [0, 1, 3, 1],
        [5, 1, 1, 1]
    ]

    "2 and 3 are domiant cell"
    assert 2 == solve(grid)

def test_solve_4x5():
    grid = [
        [0, 1, 1, 1, 9],
        [1, 2, 1, 1, 0],
        [0, 1, 3, 1, 0],
        [5, 1, 1, 1, 0]
    ]

    "2, 3, 9 are domiant cell"
    assert 3 == solve(grid)
