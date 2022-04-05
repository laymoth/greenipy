import os
import sys
import random

xd = open('list.txt')
original_stdout = sys.stdout
data = xd.read().split('\n')
random = random.choice(data)

with open('out', 'w') as f:
    sys.stdout = f
    print(random)
    sys.stdout = original_stdout
    
os.system('bash run.sh')
os.system('git add -A')
os.system('git commit -F out -s')
