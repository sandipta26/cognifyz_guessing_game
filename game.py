import tkinter as tk
import random

# Generate random number
number_to_guess = random.randint(1, 100)
attempts_p1 = 0
attempts_p2 = 0
current_player = 1
player1_name = ""
player2_name = ""

def start_game():
    global player1_name, player2_name
    player1_name = entry_p1.get()
    player2_name = entry_p2.get()
    if player1_name.strip() == "" or player2_name.strip() == "":
        instructions.config(text="⚠️ Please enter both names!", fg="yellow")
        return
    # Hide name entry widgets
    entry_p1.pack_forget()
    entry_p2.pack_forget()
    start_button.pack_forget()
    name_label1.pack_forget()
    name_label2.pack_forget()
    # Show game widgets
    instructions.config(
        text=f"🎮 Game Rules:\n"
             f"1. {player1_name} and {player2_name} will take turns guessing.\n"
             f"2. The secret number is between 1 and 100.\n"
             f"3. Each guess counts as an attempt.\n"
             f"4. The first to guess correctly wins!\n"
             f"👉 {player1_name} goes first.",
        fg="white", justify="left"
    )
    entry.pack(pady=20)
    guess_button.pack(pady=20)
    result_label.pack(pady=30)
    exit_button.pack(pady=20)

def check_guess():
    global attempts_p1, attempts_p2, current_player
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="⚠️ Please enter a valid number!", fg="yellow")
        return

    if current_player == 1:
        attempts_p1 += 1
        if guess < number_to_guess:
            result_label.config(text=f"{player1_name}: 📉 Too low! Attempts: {attempts_p1}", fg="orange")
            current_player = 2
            instructions.config(text=f"Now it's {player2_name}'s turn!")
        elif guess > number_to_guess:
            result_label.config(text=f"{player1_name}: 📈 Too high! Attempts: {attempts_p1}", fg="red")
            current_player = 2
            instructions.config(text=f"Now it's {player2_name}'s turn!")
        else:
            result_label.config(text=f"🎉 {player1_name} wins in {attempts_p1} attempts!", fg="lime")
            guess_button.config(state="disabled")
    else:
        attempts_p2 += 1
        if guess < number_to_guess:
            result_label.config(text=f"{player2_name}: 📉 Too low! Attempts: {attempts_p2}", fg="orange")
            current_player = 1
            instructions.config(text=f"Now it's {player1_name}'s turn!")
        elif guess > number_to_guess:
            result_label.config(text=f"{player2_name}: 📈 Too high! Attempts: {attempts_p2}", fg="red")
            current_player = 1
            instructions.config(text=f"Now it's {player1_name}'s turn!")
        else:
            result_label.config(text=f"🎉 {player2_name} wins in {attempts_p2} attempts!", fg="lime")
            guess_button.config(state="disabled")

# Create window
root = tk.Tk()
root.title("⚔️ Duel of Numbers ⚔️")
root.attributes('-fullscreen', True)
root.configure(bg="#0d0f1a")

# Heading
heading = tk.Label(root, text="⚔️ Duel of Numbers ⚔️",
                   font=("Arial", 40, "bold"), fg="#00ffcc", bg="#0d0f1a")
heading.pack(pady=30)

# Instructions
instructions = tk.Label(root, text="Enter names of two players to begin!",
                        font=("Arial", 20), fg="white", bg="#0d0f1a", justify="left")
instructions.pack(pady=20)

# Player name entries
name_label1 = tk.Label(root, text="Player 1 Name:", font=("Arial", 18), fg="white", bg="#0d0f1a")
name_label1.pack()
entry_p1 = tk.Entry(root, font=("Arial", 20), justify="center")
entry_p1.pack(pady=10)

name_label2 = tk.Label(root, text="Player 2 Name:", font=("Arial", 18), fg="white", bg="#0d0f1a")
name_label2.pack()
entry_p2 = tk.Entry(root, font=("Arial", 20), justify="center")
entry_p2.pack(pady=10)

start_button = tk.Button(root, text="Start Game", font=("Arial", 20, "bold"),
                         bg="#00ccff", fg="black", command=start_game)
start_button.pack(pady=20)

# Game widgets (hidden until start)
entry = tk.Entry(root, font=("Arial", 24), justify="center")
guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 20, "bold"),
                         bg="#00ccff", fg="black", command=check_guess)
result_label = tk.Label(root, text="", font=("Arial", 24, "bold"), fg="white", bg="#0d0f1a")

# Exit button
exit_button = tk.Button(root, text="Exit Game", font=("Arial", 18, "bold"),
                        bg="red", fg="white", command=root.destroy)

# Run the game
root.mainloop()
