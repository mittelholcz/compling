#! /usr/bin/env python3
"""Simple shell.
"""

import subprocess

while True:
    try:
        inp = input('--> ')
        if inp:
            subprocess.run(inp.split())
    except EOFError as ex:
        break
    except Exception as ex:
        print(ex)
        continue
print()

