import random
from datetime import datetime
from pathlib import Path

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

inside_main = False
last_print_index = None
brace_depth = 0

# Locate the last print statement inside main()
for i, line in enumerate(lines):
    if "main(" in line:
        inside_main = True
    
    if inside_main:
        brace_depth += line.count("{") - line.count("}")
        
        if "System.out.println" in line:
            last_print_index = i

        if brace_depth == 0:
            break

if last_print_index is None:
    raise SystemExit("Error: No print statement found inside main().")

# Replacement line
new_line = f'        System.out.println("CoffeeBot: {pun} [{timestamp}]");'

# Replace the last println statement
lines[last_print_index] = new_line

JAVA_FILE.write_text("\n".join(lines))

print(f"Replaced last print statement with: {pun}")
