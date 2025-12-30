import re
import random


class Board:
    def __init__(self, verbose=False):
        self.state = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.verbose = verbose

    def __getitem__(self, i):
        return self.state[i]

    def __str__(self):
        flat = [c if c else ' ' for row in self.state for c in row]
        return (
            "----------\n"
            f"| {flat[0]} | {flat[1]} | {flat[2]} |\n"
            "|---------\n"
            f"| {flat[3]} | {flat[4]} | {flat[5]} |\n"
            "|---------\n"
            f"| {flat[6]} | {flat[7]} | {flat[8]} |\n"
            "---------"
        )

    def reset(self):
        self.state = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]

    def check_win(self, player):
        return (
            any(all(self.state[i][j] == player for j in range(3)) for i in range(3)) or
            any(all(self.state[i][j] == player for i in range(3)) for j in range(3)) or
            all(self.state[i][i] == player for i in range(3)) or
            all(self.state[i][2 - i] == player for i in range(3))
        )

    def check_draw(self):
        return all(self.state[i][j] != '' for i in range(3) for j in range(3))

    def check_gameover(self):
        if self.check_win('o'):
            print("O wins!")
            return True
        if self.check_win('x'):
            print("X wins!")
            return True
        if self.check_draw():
            print("Draw!")
            return True
        return False


def ai_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    return random.choice(empty)


def get_player_move():
    move = input("Enter move (row col): ")
    return list(map(int, re.findall(r'\d+', move)))


def play_game():
    board = Board(verbose=True)

    while True:
        # AI move (O)
        r, c = ai_move(board)
        board[r][c] = 'o'
        print("AI played:", r, c)
        print(board)

        if board.check_gameover():
            break

        # Player move (X)
        while True:
            r, c = get_player_move()
            if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == '':
                board[r][c] = 'x'
                break
            else:
                print("Invalid move, try again.")

        print(board)

        if board.check_gameover():
            break


if __name__ == "__main__":
    while True:
        play_game()
        print("To quit, press q. To play again, press any key.")
        if input() == 'q':
            break
