import tkinter as tk
from random import randint

class DiceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller 🎲")
        self.root.geometry("300x250")
        self.root.configure(bg="#282c34")

        # Title Label
        self.label_title = tk.Label(root, text="Roll the Dice!", font=("Arial", 16, "bold"), bg="#282c34", fg="white")
        self.label_title.pack(pady=10)

        # Dice Result Display
        self.result_label = tk.Label(root, text="🎲", font=("Arial", 50), bg="#282c34", fg="white")
        self.result_label.pack(pady=10)

        # Roll Button
        self.roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14, "bold"), bg="#61afef", fg="white", 
                                     activebackground="#528bbd", relief="raised", padx=10, pady=5, command=self.roll_dice)
        self.roll_button.pack(pady=20)

    def roll_dice(self):
        result = randint(1, 6)  # Roll a standard 6-sided dice
        self.result_label.config(text=f"🎲 {result}")

# Main loop
root = tk.Tk()
app = DiceGUI(root)
root.mainloop()
