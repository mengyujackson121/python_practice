import sys

def check_unique(line):
    for each in line:
        if line.count(each) != 1:
            return False
    return True

lines = open(sys.argv[-1], 'r').readlines()

for line in lines:
    if len(line) > 128:
        print("False")
    else:
        print(check_unique(line))