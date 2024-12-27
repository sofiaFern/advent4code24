
with open('challenge_inputs/day4_input.csv', 'r') as file:
    input_string = file.read()

def string_to_grid(input_string):
    return [list(line) for line in input_string.splitlines()]

def check_word_in_grid(grid, word):

    count_xmas = 0

    def check_word(line, word):
        return line.count(word) + line.count(word[::-1])

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # checking rows
    for row in grid:
        count_xmas += check_word(''.join(row), word)

    # checking columns
    for col in range(cols):
        column = ''.join(grid[row][col] for row in range(rows))
        #print(column)
        col_xmas_count = check_word(column, word)
        # print(f'col count {col_xmas_count}')
        count_xmas+= col_xmas_count

    # checking diagonals
    def get_diagonals(grid):
        diagonals = []

        # Top-left to bottom-right diagonals
        for d in range(rows + cols - 1):
            diagonal = []
            for row in range(rows):
                col = d - row
                if 0 <= col < cols:
                    diagonal.append(grid[row][col])
            if diagonal:
                diagonals.append(''.join(diagonal))

        # Top-right to bottom-left diagonals
        for d in range(rows + cols - 1):
            diagonal = []
            for row in range(rows):
                col = d - row
                if 0 <= col < cols:
                    diagonal.append(grid[row][cols - 1 - col])
            if diagonal:
                diagonals.append(''.join(diagonal))

        return diagonals

    diagonals = get_diagonals(grid)
    for diagonal in diagonals:
        count_xmas += check_word(diagonal, word)

    return count_xmas

# PART 1
grid = string_to_grid(input_string)
print(check_word_in_grid(grid, 'XMAS'))