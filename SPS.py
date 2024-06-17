import tkinter as tk
from tkinter import messagebox
import random

class StonePaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stone-Paper-Scissors")
        self.root.configure(bg="#003C43")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#003C43")
        self.frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.label = tk.Label(self.frame, text="Choose your move:", bg="#003C43", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'))
        self.label.pack(pady=10, fill=tk.X)
        
        self.moves_frame = tk.Frame(self.frame, bg="#003C43")
        self.moves_frame.pack(pady=10, fill=tk.X)
        
        self.stone_btn = tk.Button(self.moves_frame, text="Stone", command=lambda: self.play_game("Stone"), bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.stone_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.paper_btn = tk.Button(self.moves_frame, text="Paper", command=lambda: self.play_game("Paper"), bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.paper_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.scissors_btn = tk.Button(self.moves_frame, text="Scissors", command=lambda: self.play_game("Scissors"), bg="#135D66", fg="#E3FEF7", font=('Times New Roman', 18, 'bold'), borderwidth=0)
        self.scissors_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.result_label = tk.Label(self.frame, text="", bg="#77B0AA", fg="#003C43", font=('Times New Roman', 18, 'bold'))
        self.result_label.pack(pady=10, fill=tk.X)
    
    def play_game(self, user_move):
        moves = ["Stone", "Paper", "Scissors"]
        computer_move = random.choice(moves)
        result = self.determine_winner(user_move, computer_move)
        self.result_label.config(text=f"You: {user_move} | Computer: {computer_move} | {result}")
    
    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a Tie!"
        elif (user == "Stone" and computer == "Scissors") or (user == "Paper" and computer == "Stone") or (user == "Scissors" and computer == "Paper"):
            return "You Win!"
        else:
            return "You Lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = StonePaperScissorsApp(root)
    root.mainloop()
