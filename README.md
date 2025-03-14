Fantasy Football Desktop App 🏈
An open-source fantasy football ranking application that allows users to customize their league settings and rankings based on ESPN or Yahoo rules.

Features Implemented So Far
✅ League Management

Users can create multiple leagues, name them, and choose between ESPN or Yahoo formats.
Leagues are saved locally in a JSON file for persistent customization.
✅ Custom Scoring System

Each league has its own custom scoring rules (e.g., Passing TDs, Receptions, Defensive Points).
Users can edit and save scoring settings, which dynamically update player rankings.
✅ Player Rankings

Rankings are generated based on user-defined scoring settings.
Basic player data is currently hardcoded (to be replaced with a live data source).
Planned Features 🚀
🛠 Edit & Delete Leagues – Allow users to modify league names, settings, or remove leagues.
🛠 Live Player Data – Integrate an API for real-time player stats and projections.
🛠 Draft Recommendations – Suggest the best available players based on custom scoring.
🛠 Improved UI – Enhance the interface with better design and sorting functionality.

How to Run the App
Clone the repository:
sh
Copy
Edit
git clone https://github.com/YOUR_GITHUB_USERNAME/fantasy-football-app.git
cd fantasy-football-app
Install dependencies:
sh
Copy
Edit
conda activate base
pip install pandas tk
Run the app:
sh
Copy
Edit
python fantasy_football.py
Contributing
This is an open-source project! Feel free to submit issues or contribute by making pull requests.