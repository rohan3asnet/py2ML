from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text()
# print(contents)

#acessing a file's lines
lines=contents.splitlines()
#woring with file's contents
pi_string=''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))

#writing to a file
#writing a single line
path.write_text('PI is really intresting value.')

