import socket
import random
import threading
import requests

# Function to fetch a random word from the Random Word API
def fetch_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        if response.status_code == 200:
            word = response.json()[0]
            return word
        else:
            return None
    except Exception as e:
        print(f"Error fetching word: {e}")
        return None

# Function to handle each client connection
def handle_client(conn, addr):
    print(f"A client connected from {addr}")
    
    conn.send("Welcome to the word guessing game! Please enter your name: ".encode())
    name = conn.recv(1024).decode().strip()
    print(f"{name} joined the game.")
    
    word_to_guess = fetch_random_word()
    if not word_to_guess:
        conn.send("Error fetching word. Please try again later.".encode())
        conn.close()
        return
    
    guessed_word = ['_'] * len(word_to_guess)
    attempts_left = 6
    guessed_letters = set()
    
    conn.send(f"Hi {name}, the word has {len(word_to_guess)} letters. You have {attempts_left} attempts left. Let's start!".encode())
    
    while attempts_left > 0 and '_' in guessed_word:
        conn.send((" ".join(guessed_word) + f" | Attempts left: {attempts_left}").encode())
        guess = conn.recv(1024).decode().lower()
        
        if not guess or guess == 'exit':
            break
        
        if len(guess) != 1 or not guess.isalpha():
            conn.send("Invalid input. Please guess a single letter.".encode())
            continue
        
        if guess in guessed_letters:
            conn.send(f"You've already guessed '{guess}'. Try a different letter.".encode())
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
            conn.send(f"Good guess! '{guess}' is in the word.".encode())
        else:
            attempts_left -= 1
            conn.send(f"Wrong guess! '{guess}' is not in the word. You have {attempts_left} attempts left.".encode())
    
    if '_' not in guessed_word:
        conn.send(f"Congratulations, {name}! You guessed the word: {word_to_guess}".encode())
    else:
        conn.send(f"Game over, {name}! You've run out of attempts. The word was: {word_to_guess}".encode())
    
    conn.close()
    print(f"{name} from {addr} has disconnected.")

host = '127.0.0.1'
port = 8002

s = socket.socket()
s.bind((host, port))
s.listen(5)  # Allow up to 5 clients to connect

print('Server is running...')

while True:
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
