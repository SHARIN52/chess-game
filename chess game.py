import random

class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.turn = 'white'
        self.game_over = False

    def create_board(self):
        # Initialize an 8x8 board with pieces in starting positions
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        return board

    def print_board(self):
        print("  a b c d e f g h")
        for i in range(8):
            print(str(8 - i) + " " + " ".join(self.board[i]) + " " + str(8 - i))
        print("  a b c d e f g h")

    def is_valid_move(self, move):
        # Basic move validation
        if len(move) != 4:
            return False
        start_col, start_row, end_col, end_row = move
        start_col = ord(start_col) - ord('a')
        end_col = ord(end_col) - ord('a')
        start_row = 8 - int(start_row)
        end_row = 8 - int(end_row)

        if 0 <= start_col < 8 and 0 <= start_row < 8 and 0 <= end_col < 8 and 0 <= end_row < 8:
            piece = self.board[start_row][start_col]
            if (self.turn == 'white' and piece.isupper()) or (self.turn == 'black' and piece.islower()):
                return True
        return False

    def make_move(self, move):
        start_col, start_row, end_col, end_row = move
        start_col = ord(start_col) - ord('a')
        end_col = ord(end_col) - ord('a')
        start_row = 8 - int(start_row)
        end_row = 8 - int(end_row)

        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = " "
        self.board[end_row][end_col] = piece

    def get_all_possible_moves(self):
        # Simplified: Return all possible moves randomly (not actual chess logic)
        moves = []
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if (self.turn == 'white' and piece.isupper()) or (self.turn == 'black' and piece.islower()):
                    for di in [-1, 1]:
                        for dj in [-1, 1]:
                            new_i, new_j = i + di, j + dj
                            if 0 <= new_i < 8 and 0 <= new_j < 8:
                                moves.append((chr(j + ord('a')) + str(8 - i) +
                                              chr(new_j + ord('a')) + str(8 - new_i)))
        return moves

    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'

    def play(self):
        while not self.game_over:
            self.print_board()
            if self.turn == 'white':
                move = input("Enter your move (e.g., e2e4): ").strip()
                if self.is_valid_move(move):
                    self.make_move(move)
                    self.switch_turn()
                else:
                    print("Invalid move. Try again.")
            else:
                print("Computer's turn:")
                possible_moves = self.get_all_possible_moves()
                if possible_moves:
                    move = random.choice(possible_moves)
                    print(f"Computer plays: {move}")
                    self.make_move(move)
                    self.switch_turn()
                else:
                    self.game_over = True
                    print("No more moves. Game over!")

if __name__ == "__main__":
    game = ChessGame()
    game.play()
