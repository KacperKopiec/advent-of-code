import os
import re

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip() 

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches = re.findall(pattern, f)

ans = 0
add = True
for line in matches:
    if line[0] == 'm' and add:
        x, y = line[4:-1].split(',')
        ans += int(x) * int(y)
    elif line == "do()":
        add = True
    else:
        add = False
print(ans)