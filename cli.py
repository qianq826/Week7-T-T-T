import random

class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_full(self):
        return all(all(cell != " " for cell in row) for row in self.board)

    def update_board(self, move, symbol):
        if self.board[move[0]][move[1]] == " ":
            self.board[move[0]][move[1]] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or \
               all(self.board[j][i] == symbol for j in range(3)):
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        return False

class Player:
    def get_move(self, board):
        pass

class Human:
    def get_move(self, board):
        move = input("Enter your move (row col): ").split()
        return int(move[0]), int(move[1])

class Bot:
    def get_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board.board[i][j] == " "]
        return random.choice(empty_cells)

class Game:
    def __init__(self, playerX, playerO):
        self.board = Board()
        self.playerX = playerX
        self.playerO = playerO
        self.players = [playerX, playerO]
        self.current_player = 0

    def run(self):
        while True:
            self.board.display()
            move = self.players[self.current_player].get_move(self.board)
            if self.board.update_board(move, "X" if self.current_player == 0 else "O"):
                if self.board.check_winner("X" if self.current_player == 0 else "O"):
                    print(f"Player {'X' if self.current_player == 0 else 'O'} wins!")
                    break
                if self.board.is_full():
                    print("It's a draw!")
                    break
                self.current_player = 1 - self.current_player
            else:
                print("Invalid move, try again.")

# Example usage
player_choice = input("Choose 1 for single player or 2 for two players: ")
if player_choice == "1":
    game = Game(Human(), Bot())
else:
    game = Game(Human(), Human())
game.run()
