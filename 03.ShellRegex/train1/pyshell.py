#! /usr/bin/env python3
"""Simple python shell.
"""

while True:
    try:
        inp = input('--> ')
        exec(inp)
    except EOFError as ex:
        break
    except Exception as ex:
        print(ex)
        continue
print()

