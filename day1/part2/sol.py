def parseStrNum(s):
    if s.startswith('one'):
        return ['1', 3]
    elif s.startswith('two'):
        return ['2', 3]
    elif s.startswith('three'):
        return ['3', 5]
    elif s.startswith('four'):
        return ['4', 4]
    elif s.startswith('five'):
        return ['5', 4]
    elif s.startswith('six'):
        return ['6', 3]
    elif s.startswith('seven'):
        return ['7', 5]
    elif s.startswith('eight'):
        return ['8', 5]
    elif s.startswith('nine'):
        return ['9', 4]
    
    return None

lines = [] # create list
with open("input.txt") as file:
# with open("d1p2.txt") as file: # easier test case
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

        elif lines[i][j] == 'o' or lines[i][j] == 't' or lines[i][j] == 'f' or lines[i][j] == 's' or lines[i][j] == 'e' or lines[i][j] == 'n':
            parsed = parseStrNum(lines[i][j:])

            if parsed is not None:
                strNum = parsed[0]

                if numFound is 0: # find the first number
                    first.append(strNum)
                    last.append(first[-1])
                    numFound += 1
                
                else: # find the last number
                    last[-1] = strNum      
                
                j += parsed[1]
        j += 1

sum = 0
for i in range(len(first)):
    concat = first[i] + last[i]
    sum += int(concat)
print(sum)