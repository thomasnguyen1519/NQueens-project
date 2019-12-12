

class NQueens:

    def __init__(self, n):
        self.__board = []
        self.__rows = set()
        self.__cols = set()
        self.__diags = set()
        self.__antidiags = set()
        # initialize the board to empty state
        for i in range(n):
            self.__board.append(bytearray("-" * n, 'utf-8'))

    # Returns True if a queen can be placed safely, otherwise False
    def is_safe(self, row, col):
        return (row not in self.__rows and col not in self.__cols and
            -1 * row + col not in self.__antidiags and
            row + col not in self.__diags)

    # Places queen at specified position
    def place(self, row, col):
        if row < 0 or row >= len(__board) or col < 0 or col >= len(__board):
            print("Invalid row or column.")
            print("Row ->", row)
            print("Column ->", col)
        else:
            self.__rows.add(row)
            self.__cols.add(col)
            self.__diags.add(row + col)
            self.__antidiags.add(-1 * row + col)
            self.__board[row][col] = ord("Q")

    # Removes queen from specified position
    def remove(self, row, col):
        if row < 0 or row >= len(__board) or col < 0 or col >= len(__board):
            print("Invalid row or column.")
            print("Row ->", row)
            print("Column ->", col)
        else:
            self.__rows.remove(row)
            self.__cols.remove(col)
            self.__diags.remove(row + col)
            self.__antidiags.remove(-1 * row + col)
            self.__board[row][col] = ord("-")

    # Prints the current state of the board
    def print_state(self):
        print([line.decode() for line in self.__board])
