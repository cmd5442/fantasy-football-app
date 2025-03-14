import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import json
import os

# File to store league settings
SETTINGS_FILE = "leagues.json"

# Load existing leagues
if os.path.exists(SETTINGS_FILE):
    with open(SETTINGS_FILE, "r") as f:
        leagues = json.load(f)
else:
    leagues = {}

# Save leagues to file
def save_leagues():
    with open(SETTINGS_FILE, "w") as f:
        json.dump(leagues, f, indent=4)

# Function to add a new league
def add_league():
    name = league_name_var.get()
    platform = platform_var.get()
    if not name:
        messagebox.showerror("Error", "League name cannot be empty.")
        return
    if name in leagues:
        messagebox.showerror("Error", "League already exists.")
        return
    leagues[name] = {
        "platform": platform,
        "scoring": {
            "Passing TD": 4, "Interception": -2, "Passing Yards": 0.04,
            "Rushing TD": 6, "Rushing Yards": 0.1, "Reception": 0.5,
            "Receiving TD": 6, "FG Made": 3, "PAT Made": 1,
            "Sack": 1, "Interception Return TD": 6, "Fumble Return TD": 6,
            "Safety": 2, "Blocked Kick TD": 6, "0 Points Allowed": 7
        }
    }
    save_leagues()
    league_dropdown["values"] = list(leagues.keys())
    messagebox.showinfo("Success", f"League '{name}' added!")

# Function to customize scoring settings
def customize_scoring():
    league = selected_league_var.get()
    if not league or league not in leagues:
        messagebox.showerror("Error", "Select a valid league.")
        return
    
    def save_scoring():
        for key, entry in scoring_entries.items():
            try:
                leagues[league]["scoring"][key] = float(entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for {key}.")
                return
        save_leagues()
        scoring_window.destroy()
        messagebox.showinfo("Success", "Scoring settings updated!")
    
    scoring_window = tk.Toplevel(root)
    scoring_window.title("Customize Scoring")
    scoring_entries = {}
    row = 0
    for category, value in leagues[league]["scoring"].items():
        tk.Label(scoring_window, text=category).grid(row=row, column=0)
        entry = tk.Entry(scoring_window)
        entry.insert(0, value)
        entry.grid(row=row, column=1)
        scoring_entries[category] = entry
        row += 1
    tk.Button(scoring_window, text="Save", command=save_scoring).grid(row=row, column=0, columnspan=2)

# Function to fetch player data (replace with API later)
def fetch_player_data():
    data = [
        {'Name': 'Player A', 'Position': 'QB', 'Passing TD': 3, 'Interception': 1, 'Passing Yards': 300},
        {'Name': 'Player B', 'Position': 'RB', 'Rushing TD': 2, 'Rushing Yards': 100},
        {'Name': 'Player C', 'Position': 'WR', 'Reception': 6, 'Receiving TD': 1},
    ]
    return pd.DataFrame(data)

# Function to update rankings
def update_rankings():
    league = selected_league_var.get()
    if not league or league not in leagues:
        messagebox.showerror("Error", "Select a valid league.")
        return
    
    scoring = leagues[league]["scoring"]
    df = fetch_player_data()
    df['Points'] = 0
    for key in scoring.keys():
        if key in df.columns:
            df['Points'] += df[key] * scoring[key]
    
    df = df.sort_values(by='Points', ascending=False)
    
    for row in tree.get_children():
        tree.delete(row)
    
    for _, row in df.iterrows():
        tree.insert('', 'end', values=(row['Name'], row['Position'], row['Points']))

# Create main window
root = tk.Tk()
root.title("Fantasy Football Rankings")
root.geometry("500x500")

# League Management
tk.Label(root, text="Add New League:").pack()
league_name_var = tk.StringVar()
platform_var = tk.StringVar(value="ESPN")
tk.Entry(root, textvariable=league_name_var).pack()
ttk.Combobox(root, textvariable=platform_var, values=["ESPN", "Yahoo"]).pack()
tk.Button(root, text="Add League", command=add_league).pack()

# League Selection
tk.Label(root, text="Select League:").pack()
selected_league_var = tk.StringVar()
league_dropdown = ttk.Combobox(root, textvariable=selected_league_var, values=list(leagues.keys()))
league_dropdown.pack()

# Button to update rankings
update_button = tk.Button(root, text="Update Rankings", command=update_rankings)
update_button.pack()

# Button to customize scoring
tk.Button(root, text="Customize Scoring", command=customize_scoring).pack()

# Table for displaying rankings
tree = ttk.Treeview(root, columns=("Name", "Position", "Points"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Position", text="Position")
tree.heading("Points", text="Points")
tree.pack(fill='both', expand=True)

# Run the app
root.mainloop()
