import adventutils


def part1(file):
    print("Part 1")
    game = adventutils.file_contents(file)
    calls = game[0].removesuffix("\n").split(",")
    boards = list()
    current_board = list()
    for index in range(2, len(game)):
        if game[index] == "\n":
            boards.append(current_board)
            current_board = list()
            continue
        nums = game[index].removesuffix("\n").split(" ")
        current_row = list()
        for num in nums:
            if num != "":
                current_row.append(num)
        current_board.append(current_row)
    boards.append(current_board)
    for num in calls:
        call(boards, num)
        board, row, column = validate(boards)
        if board is not None:
            print(score_unmarked(board, num))
            break


def part2(file):
    print("Part 2")
    game = adventutils.file_contents(file)
    calls = game[0].removesuffix("\n").split(",")
    boards = list()
    current_board = list()
    for index in range(2, len(game)):
        if game[index] == "\n":
            boards.append(current_board)
            current_board = list()
            continue
        nums = game[index].removesuffix("\n").split(" ")
        current_row = list()
        for num in nums:
            if num != "":
                current_row.append(num)
        current_board.append(current_row)
    boards.append(current_board)
    for num in calls:
        call(boards, num)
        board, row, column = validate(boards)
        while board is not None:
            if board is not None and len(boards) > 1:
                boards.remove(board)
                board, row, column = validate(boards)
            elif board is not None and len(boards) == 1:
                print(score_unmarked(board, num))
                return


def remove_all(collection, val):
    for index in range(len(collection)):
        collection[index] = collection[index].removeprefix(val)


def call(boards, num):
    for board in boards:
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == num:
                    board[row][column] += "x"


def validate(boards):
    for board in boards:
        for row in range(len(board)):
            if validate_row(board, row):
                return board, row, None
        for column in range(len(board[0])):
            if validate_column(board, column):
                return board, None, column
    return None, None, None


def validate_row(board, row):
    if board[row][0].endswith("x"):
        for column in range(len(board[row])):
            if not board[row][column].endswith("x"):
                return False
        return True
    return False


def validate_column(board, column):
    if board[0][column].endswith("x"):
        for row in range(len(board)):
            if not board[row][column].endswith("x"):
                return False
        return True
    return False


def score(board, row, column):
    total = 0
    if row is not None:
        for column in range(len(board[row])):
            total += int(board[row][column].removesuffix("x"))
    elif column is not None:
        for row in range(len(board)):
            total += int(board[row][column].removesuffix("x"))
    return total


def score_unmarked(board, last_called):
    total = 0
    for row in board:
        for column in row:
            if not column.endswith("x"):
                total += int(column)
    return total * int(last_called)


if __name__ == "__main__":
    part1("./data/day4part1.txt")
    part2("./data/day4part1.txt")
