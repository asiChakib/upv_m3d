import sys

# Fake the command-line arguments
sys.argv = ["zzz.py", "arg1", "arg2", "arg3"]

with open("zzz.py") as f:
    code = f.read()
    exec(code)
