import socket
import tkinter as tk
from tkinter import messagebox

class TicTacToeClient:
    def __init__(self, master, server_ip, server_port):
        self.master = master
        self.server_ip = server_ip
        self.server_port = server_port

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player_mark = 'X'

        self.create_widgets()
        self.connect_to_server()
    
    def create_widgets(self):
        self.buttons = [[None]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text='', font=('Arial', 30), width=4, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
        self.status_label = tk.Label(self.master, text='', font=('Arial', 14))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def connect_to_server(self):
        self.socket = socket.socket()
        self.socket.connect((self.server_ip, self.server_port))
        self.receive_message()

    def receive_message(self):
        while True:
            message = self.socket.recv(1024).decode()
            print("Received message:", message)  # Add this line for debugging
            if "Your move" in message:
                self.status_label.config(text="Your move")
            elif "Congratulations!" in message or "Sorry, you lose!" in message or "It's a tie!" in message:
                self.status_label.config(text=message)
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j].config(state=tk.DISABLED)
                break
            elif message.startswith('Invalid'):
                messagebox.showerror("Error", message)
            else:
                # row, col, mark = message.split()
                # row, col = int(row), int(col)
                # self.board[row][col] = mark
                # self.buttons[row][col].config(text=mark, state=tk.DISABLED)
                # self.status_label.config(text="Waiting for opponent's move")
                pass  # Temporarily comment out the unpacking code

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player_mark
            self.buttons[row][col].config(text=self.player_mark, state=tk.DISABLED)
            self.socket.send(f"{row} {col}".encode())
            self.status_label.config(text="Waiting for opponent's move")
        else:
            messagebox.showerror("Error", "Invalid move. Try again.")


def main():
    server_ip = '127.0.0.1'
    server_port = 8002

    root = tk.Tk()
    root.title("Tic Tac Toe")
    tic_tac_toe_client = TicTacToeClient(root, server_ip, server_port)
    root.mainloop()

if __name__ == "__main__":
    main()
