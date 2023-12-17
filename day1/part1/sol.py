lines = [] # create list
with open("input.txt") as file:
# with open("d1p1.txt") as file: # easier test case
    lines = file.readlines()

first, last = [], []
for i in range(len(lines)):
    numFound = 0

    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            if numFound is 0: # find the first number
                first.append(lines[i][j])
                last.append(first[-1])
                numFound += 1

            else: # find the last number
                last[-1] = lines[i][j]

sum = 0
for i in range(len(first)):
    concat = first[i] + last[i]
    sum += int(concat)
print(sum)