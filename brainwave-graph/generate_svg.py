import os
from datetime import date, timedelta

# 🔁 Replace with your name and GitHub email
author = 'Sneha Devkota'
email = 'snehadevkota534@gmail.com'

# Brainwave pattern: higher = more commits
brainwave = [0, 1, 3, 5, 3, 1, 0] * 7  # 49 days of wave

# Start date = 49 days ago
start_date = date.today() - timedelta(days=len(brainwave))

for i, commits in enumerate(brainwave):
    day = start_date + timedelta(days=i)
    for c in range(commits):
        with open("log.txt", "a") as f:
            f.write(f"{day} - wave {c+1}\n")
        os.system(f'git add log.txt')
        os.system(f'git commit --date="{day} 12:00:00" --author="{author} <{email}>" -m "Brainwave commit {c+1}"')
