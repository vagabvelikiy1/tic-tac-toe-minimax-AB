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
        rows = []
        for r in self.state:
            rows.append(" | ".join(c if c else ' ' for c in r))
        return "\n---------\n".join(rows)

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

    def game_over(self):
        if self.check_win('x'):
            print("X wins!")
            return True
        if self.check_win('o'):
            print("O wins!")
            return True
        if self.check_draw():
            print("Draw!")
            return True
        return False


def random_ai_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    return random.choice(empty)


def get_player_move():
    move = input("Enter move (row col): ")
    return list(map(int, re.findall(r'\d+', move)))


def play_game():
    board = Board(verbose=True)

    while True:
        print(board)

        # Player move (O)
        while True:
            r, c = get_player_move()
            if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == '':
                board[r][c] = 'o'
                break
            else:
                print("Invalid move, try again.")

        if board.game_over():
            print(board)
            break

        # AI move (X)
        r, c = random_ai_move(board)
        board[r][c] = 'x'
        print("\nAI played:", r, c)

        if board.game_over():
            print(board)
            break


if __name__ == "__main__":
    while True:
        play_game()
        if input("Press q to quit, anything else to play again: ") == 'q':
            break
