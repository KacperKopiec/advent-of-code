import os
import re

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip() 

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, f)

ans = 0
for line in matches:
    x, y = line[4:-1].split(',')
    ans += int(x) * int(y)
print(ans)