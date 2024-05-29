import socket
import threading

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-----')

def check_winner(board, mark):
    # Check rows
    for row in board:
        if all(cell == mark for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def handle_client(conn, addr, player):
    print(f"Player {player} connected from {addr}")

    conn.send(f"You are player {player}. Waiting for another player to join...".encode())

    # Wait for both players to join
    players_ready_event.wait()

    conn.send("Both players have joined. Game starting...".encode())

    while True:
        conn.send("Your move. Enter row (0-2) and column (0-2) separated by a space (e.g., '1 2'): ".encode())
        move = conn.recv(1024).decode()
        if move.lower() == 'exit':
            break
        try:
            row, col = map(int, move.split())
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = 'X' if player == 1 else 'O'
                print_board(board)
                if check_winner(board, 'X'):
                    conn.send("Congratulations! You win!".encode())
                    break
                elif check_winner(board, 'O'):
                    conn.send("Sorry, you lose! Player 1 wins.".encode())
                    break
                elif all(cell != ' ' for row in board for cell in row):
                    conn.send("It's a tie!".encode())
                    break
                else:
                    conn.send("Waiting for the other player's move...".encode())
                    players_ready_event.wait()
            else:
                conn.send("Invalid move. Try again.".encode())
        except (ValueError, IndexError):
            conn.send("Invalid input format. Please enter row and column as integers between 0 and 2 separated by a space.".encode())

    print(f"Player {player} from {addr} has disconnected.")
    conn.close()

host = '127.0.0.1'
port = 8002

board = initialize_board()
players_ready_event = threading.Event()

s = socket.socket()
s.bind((host, port))
s.listen(2)  # Allow up to 2 clients to connect

print('Server is running...')

player = 1
while True:
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn, addr, player)).start()
    player += 1
    if player > 2:
        players_ready_event.set()
