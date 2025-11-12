import random
from datetime import datetime
from pathlib import Path

# --- random coffee puns ---
PUNS = [
    "Commit your coffee, not your code before it compiles.",
    "Espresso yourself, then push to main.",
    "Mugs before bugs.",
    "Practicing Caffeine-Driven Development (CDD).",
    "Decaf is just a failed build.",
    "Keep calm and merge the mocha.",
    "Pull, brew, rebase, repeat.",
    "Hotfixes and hot brews keep production alive.",
    "Merge conflicts taste better with espresso.",
    "Feature freeze? Time for an iced brew.",
    "Never debug before your first cup.",
    "It’s not a bug, it’s a feature - until the coffee wears off.",
    "I like my IDE like my coffee: dark theme, no sugarcoating.",
    "Version control your caffeine intake."
]

JAVA_FILE = Path("CommitCafe.java")
if not JAVA_FILE.exists():
    raise SystemExit("Error: CommitCafe.java not found")

lines = JAVA_FILE.read_text().splitlines()
pun = random.choice(PUNS)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# find last closing brace of main()
brace_depth = 0
inside_main = False
insert_index = None

for i, line in enumerate(lines):
    if "main(" in line:
        inside_main = True
    if inside_main:
        brace_depth += line.count("{") - line.count("}")
        if brace_depth == 0:
            insert_index = i
            break

if insert_index is None:
    raise SystemExit("Error: Could not locate end of main() method.")

# build line to insert
new_line = f'        System.out.println("CoffeeBot: {pun} [{timestamp}]");'

# insert just before the closing brace
lines.insert(insert_index, new_line)

JAVA_FILE.write_text("\n".join(lines))
print(f"Injected new coffee pun line: {pun}")
