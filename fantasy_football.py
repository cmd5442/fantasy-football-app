import tkinter as tk
from tkinter import ttk
import pandas as pd

# Sample function to fetch player data (replace with actual API later)
def fetch_player_data():
    data = [
        {'Name': 'Player A', 'Position': 'RB', 'Points': 120},
        {'Name': 'Player B', 'Position': 'QB', 'Points': 150},
        {'Name': 'Player C', 'Position': 'WR', 'Points': 110},
    ]
    return pd.DataFrame(data)

# Function to update rankings based on scoring rules
def update_rankings():
    scoring = scoring_var.get()
    df = fetch_player_data()
    
    if scoring == 'PPR':
        df['Points'] *= 1.1  # Example: Boost PPR scores
    elif scoring == 'Half-PPR':
        df['Points'] *= 1.05
    
    df = df.sort_values(by='Points', ascending=False)
    
    for row in tree.get_children():
        tree.delete(row)
    
    for _, row in df.iterrows():
        tree.insert('', 'end', values=(row['Name'], row['Position'], row['Points']))

# Create main window
root = tk.Tk()
root.title("Fantasy Football Rankings")
root.geometry("400x300")

# Scoring rule selection
tk.Label(root, text="Select Scoring System:").pack()
scoring_var = tk.StringVar(value='Standard')
scoring_dropdown = ttk.Combobox(root, textvariable=scoring_var, values=['Standard', 'PPR', 'Half-PPR'])
scoring_dropdown.pack()

# Button to update rankings
update_button = tk.Button(root, text="Update Rankings", command=update_rankings)
update_button.pack()

# Table for displaying rankings
tree = ttk.Treeview(root, columns=("Name", "Position", "Points"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Position", text="Position")
tree.heading("Points", text="Points")
tree.pack(fill='both', expand=True)

# Run the app
root.mainloop()
