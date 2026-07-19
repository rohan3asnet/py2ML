from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text()
# print(contents)

#acessing a file's lines
lines=contents.splitlines()
for line in lines:
    print(line)