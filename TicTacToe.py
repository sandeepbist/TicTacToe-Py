import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg="white")
        self.canvas.pack()
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.canvas.bind("<Button-1>", self.click)
        self.draw_grid()
        self.root.mainloop()

    def draw_grid(self):
        for i in range(1, 3):
            self.canvas.create_line(100 * i, 0, 100 * i, 300, width=2)
            self.canvas.create_line(0, 100 * i, 300, 100 * i, width=2)

    def click(self, event):
        if self.game_over:
            return
        row, col = event.y // 100, event.x // 100
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.draw_symbol(row, col)
            if self.check_winner():
                self.canvas.create_text(150, 150, text=f"{self.current_player} Wins!", font=("Arial", 32), fill="green")
                self.game_over = True
            elif all(all(cell is not None for cell in row) for row in self.board):
                self.canvas.create_text(150, 150, text="It's a Draw!", font=("Arial", 32), fill="blue")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def draw_symbol(self, row, col):
        x_start, y_start = col * 100 + 10, row * 100 + 10
        x_end, y_end = col * 100 + 90, row * 100 + 90
        if self.current_player == "X":
            self.canvas.create_line(x_start, y_start, x_end, y_end, width=4, fill="red")
            self.canvas.create_line(x_start, y_end, x_end, y_start, width=4, fill="red")
        else:
            self.canvas.create_oval(x_start, y_start, x_end, y_end, width=4, outline="blue")

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True
        return False

    def reset_game(self):
        self.canvas.delete("all")
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.draw_grid()

TicTacToe()
