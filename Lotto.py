import random
import tkinter as tk

class LotteryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lottery Draw 🎟️")
        self.root.geometry("350x300")
        self.root.configure(bg="#282c34")

        # Title Label
        self.label_title = tk.Label(root, text="Lottery Ticket Draw", font=("Arial", 16, "bold"), 
                                    bg="#282c34", fg="white")
        self.label_title.pack(pady=10)

        # Winning Ticket Display
        self.result_label = tk.Label(root, text="Click to Draw 🎲", font=("Arial", 14), 
                                     bg="#282c34", fg="yellow")
        self.result_label.pack(pady=20)

        # Draw Button
        self.draw_button = tk.Button(root, text="Draw Ticket", font=("Arial", 14, "bold"), 
                                     bg="#61afef", fg="white", activebackground="#528bbd", 
                                     relief="raised", padx=10, pady=5, command=self.draw_ticket)
        self.draw_button.pack(pady=20)

    def draw_ticket(self):
        # Define the lottery list
        lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Select 4 random winning numbers/letters
        winning = random.sample(lst, 4)

        # Update label with the winning ticket
        self.result_label.config(text=f"🎉 Winning Ticket: {winning} 🎉")

# Run the GUI
root = tk.Tk()
app = LotteryGUI(root)
root.mainloop()
