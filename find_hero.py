import os
DIR = r"c:\Users\HP ZBOOK\Downloads\Golden eagle\redesign"
with open(os.path.join(DIR, "styles.css"), "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "hero" in line.lower() or "5rem" in line:
        print(f"Line {i+1}: {line.strip()}")
