# **Fantasy Football Desktop App 🏈**  
An open-source **fantasy football ranking application** that allows users to customize their league settings and rankings based on ESPN or Yahoo rules.

## **Features Implemented So Far**
✅ **League Management**  
- Users can **create multiple leagues**, name them, and choose between **ESPN** or **Yahoo** formats.  
- Leagues are **saved locally** in a JSON file for persistent customization.  

✅ **Custom Scoring System**  
- Each league has its own **custom scoring rules** (e.g., Passing TDs, Receptions, Defensive Points).  
- Users can **edit and save scoring settings**, which dynamically update player rankings.  

✅ **Player Rankings**  
- Rankings are generated based on **user-defined scoring settings**.  
- Basic player data is currently hardcoded (to be replaced with a live data source).  

## **Planned Features 🚀**  
🛠 **Edit & Delete Leagues** – Allow users to modify league names, settings, or remove leagues.  
🛠 **Live Player Data** – Integrate an API for real-time player stats and projections.  
🛠 **Draft Recommendations** – Suggest the best available players based on custom scoring.  
🛠 **Improved UI** – Enhance the interface with better design and sorting functionality.  

## **How to Run the App**  
1. **Clone the repository**:  
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/fantasy-football-app.git
   cd fantasy-football-app
   ```

2. **Install dependencies**:  
```sh
conda activate base
pip install pandas tk
```

3. **Run the app:**:  
```sh
python fantasy_football.py
```


### **This is an open-source project! Feel free to submit issues or contribute by making pull requests.**  

---

### **Steps to Update GitHub**
1. **In VS Code**, open `README.md`.
2. **Paste the markdown content** above and save it (`Ctrl+S` / `Cmd+S`).
3. **Commit & Push:**
   - Open the **Source Control (Git) panel** (`Ctrl+Shift+G`).
   - Click **"+" (Stage Changes)** next to `README.md`.
   - Enter a commit message:  
     ```
     Updated README with project details
     ```
   - Click the **✓ (checkmark) button** to commit.
   - Click **"…" > Push** to upload the changes to GitHub.

Now, when you check your GitHub repo, your **README.md** will display perfectly formatted! Let me know when you're ready to continue! 🚀
