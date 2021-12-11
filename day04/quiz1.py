import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

input_file = sys.argv[1]

data = []
with open(input_file, "r") as f:
    data = [x.rstrip() for x in f.readlines()]


def check_bingo(bingo_board_visited):
    for i in range(5):
        bingo = True
        for j in range(5):
            bingo &= bingo_board_visited[i][j]
        if bingo:
            return True

    for j in range(5):
        bingo = True
        for i in range(5):
            bingo &= bingo_board_visited[i][j]
        if bingo:
            return True


#    bingo = True
#    for i in range(5):
#        bingo &= bingo_board_visited[i][i]
#    if bingo:
#        return True
#
#    bingo = True
#    for i in range(5):
#        bingo &= bingo_board_visited[i][4-i]
#    if bingo:
#        return True
#
    return False


def get_score(board, visited, number):
    score = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                score += board[i][j]

    return score * number


inputs = [int(x) for x in data[0].split(",")]

bingo_boards = []

for i in range(1, len(data), 6):
    bingo_board = []
    bingo_board_set = set()
    for j in range(1, 6):
        numbers = [int(x) for x in data[i + j].split() if x.isdigit()]
        bingo_board.append(numbers)

    bingo_boards.append(bingo_board)

bingo_boards_visited = [[[False] * 5 for _ in range(5)]
                        for _ in range(len(bingo_boards))]

winning_board = -1
last_called_number = 0
for number in inputs:
    for k in range(len(bingo_boards)):
        bingo_board = bingo_boards[k]
        for i in range(5):
            for j in range(5):
                if bingo_board[i][j] == number:
                    bingo_boards_visited[k][i][j] = True
                    break
    winning_board_found = False
    for k in range(len(bingo_boards)):
        if check_bingo(bingo_boards_visited[k]):
            winning_board_found = True
            winning_board = k
            last_called_number = number
            break

    if winning_board_found:
        break

print(
    get_score(bingo_boards[winning_board], bingo_boards_visited[winning_board],
              last_called_number))
