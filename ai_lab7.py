# -*- coding: utf-8 -*-
"""AI_LAB7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZYeopRR-RA9yoBMu2FLfHKt71x1Wrb8F
"""

import itertools

file_path='/content/INPUT.txt'
def read_input(file_path):
    with open(file_path, 'r') as file:
        first_number = file.readline().strip()
        second_number = file.readline().strip()
        sum_number = file.readline().strip()
    return first_number, second_number, sum_number

def unique_letters(first, second, result):
    return set(first + second + result)

def evaluate_expression(first, second, result, mapping):
    first_num = ''.join(str(mapping[char]) for char in first)
    second_num = ''.join(str(mapping[char]) for char in second)
    result_num = ''.join(str(mapping[char]) for char in result)

    return int(first_num) + int(second_num) == int(result_num)

def solve_cryptarithmetic(first, second, result):
    letters = unique_letters(first, second, result)

    if len(letters) > 10:
        return None

    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        if (mapping[first[0]] == 0 or
            mapping[second[0]] == 0 or
            mapping[result[0]] == 0):
            continue

        if evaluate_expression(first, second, result, mapping):
            return mapping

    return None

def format_output(mapping, first, second, result):
    first_num = ''.join(str(mapping[char]) for char in first)
    second_num = ''.join(str(mapping[char]) for char in second)
    result_num = ''.join(str(mapping[char]) for char in result)
    return f"{first_num}+{second_num}={result_num}"

def main(file_path):
    first, second, result = read_input(file_path)
    mapping = solve_cryptarithmetic(first, second, result)

    if mapping:
        output = format_output(mapping, first, second, result)
        print(output)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main("INPUT.txt")

def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    grid = []
    for i in range(9):
        row = list(map(int, lines[i].strip().split()))
        grid.append(row)

    constraints = {}
    for line in lines[9:]:
        parts = line.strip().split(' ', 1)
        total = int(parts[0])
        positions = eval(parts[1])
        constraints[tuple(positions)] = total

    return grid, constraints

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def check_constraints(grid, constraints):
    for positions, total in constraints.items():
        sum_value = sum(grid[r][c] for r, c in positions if grid[r][c] != 0)
        if sum_value > total:
            return False
    return True

def solve_sudoku(grid, constraints):
    empty = find_empty_location(grid)
    if not empty:
        return check_constraints(grid, constraints)

    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if check_constraints(grid, constraints):
                if solve_sudoku(grid, constraints):
                    return True
            grid[row][col] = 0

    return False

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def main(input_file):
    grid, constraints = read_input_file(input_file)
    if solve_sudoku(grid, constraints):
        print_grid(grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    input_file = 'adoku.txt'
    main(input_file)