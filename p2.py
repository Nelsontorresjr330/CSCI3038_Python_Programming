import sys

with open(sys.argv[1], 'r') as f: #Opens the file from argv[1]
    lines = f.readlines()   #Stores each file line in lines

symtab = {} #Declares dictionary for symbal table
variables = {} #Declares dictionary for variables in the robot

for iter, line in enumerate(lines): #Loops through each line in Lines
    if line[0] != " ":  #If a label is found
            symtab[line[0:line.find(" ")].upper()] = iter #Place label in symtab
            temp = line[line.find(" "):len(line)] #Remakes line
            line = temp #Without the label
    line = line.upper() #Lowercases the line
    line = line[0:line.find("#")].split() #Splits it into arguments
    lines[iter] = line #Places it into new list

iter = 0    #Variable for keeping track of the iteration
x = 0       #X position
y = 0       #Y position

while iter < len(lines): #While lines are still to be read

    if lines[iter][0] == "YMOVE":   #If command is move Y
        try:
            y = y + int(lines[iter][1])
        except:
            y = y + int(variables[lines[iter][1]])
        iter += 1

    elif lines[iter][0] == "XMOVE": #If command is move X
        try:
            x = x + int(lines[iter][1])
        except:
            x = x + int(variables[lines[iter][1]])
        iter += 1

    elif lines[iter][0] == "PRINTLOC": #If command is print X & Y
        if x > 33 or y > 33:
            print("error: move off board")
        else:
            print(x, ",", y)
        iter += 1

    elif lines[iter][0] == "IF":    #If command is an IF

        if lines[iter][2] == "<":
            try:
                left = int(lines[iter][1])
                leftisint = 1
            except:
                left = lines[iter][1]
                leftisint = 0
            try:
                right = int(lines[iter][3])
                rightisint = 1
            except:
                right = lines[iter][3]
                rightisint = 0
            
            if leftisint == 0:
                left = variables[lines[iter][1]]

            if rightisint == 0:
                right = variables[lines[iter][3]]

            if int(left) < int(right):
                iter = symtab[lines[iter][4]]
            else:
                iter += 1
        elif lines[iter][2] == ">":
            try:
                left = int(lines[iter][1])
                leftisint = 1
            except:
                left = lines[iter][1]
                leftisint = 0
            try:
                right = int(lines[iter][3])
                rightisint = 1
            except:
                right = lines[iter][3]
                rightisint = 0
            
            if leftisint == 0:
                left = variables[lines[iter][1]]

            if rightisint == 0:
                right = variables[lines[iter][3]]

            if int(left) > int(right):
                iter = symtab[lines[iter][4]]
            else:
                iter += 1
        elif lines[iter][2] == "==":
            try:
                left = int(lines[iter][1])
                leftisint = 1
            except:
                left = lines[iter][1]
                leftisint = 0
            try:
                right = int(lines[iter][3])
                rightisint = 1
            except:
                right = lines[iter][3]
                rightisint = 0
            
            if leftisint == 0:
                left = variables[lines[iter][1]]

            if rightisint == 0:
                right = variables[lines[iter][3]]

            if int(left) == int(right):
                iter = symtab[lines[iter][4]]
            else:
                iter += 1
        elif lines[iter][2] == "!=":
            try:
                left = int(lines[iter][1])
                leftisint = 1
            except:
                left = lines[iter][1]
                leftisint = 0
            try:
                right = int(lines[iter][3])
                rightisint = 1
            except:
                right = lines[iter][3]
                rightisint = 0
            
            if leftisint == 0:
                left = variables[lines[iter][1]]

            if rightisint == 0:
                right = variables[lines[iter][3]]

            if int(left) != int(right):
                iter = symtab[lines[iter][4]]
            else:
                iter += 1
        else:
            print("Invalid Operator")
            quit()

    elif lines[iter][0] == "GOTO":  #If command is goto
        iter = symtab[lines[iter][1]]

    elif lines[iter][0] == "SET":   #If command is Set
        variables[lines[iter][1]] = int(lines[iter][2])
        iter += 1

    elif lines[iter][0] == "ADD":   #If command is Add
        word = lines[iter][1]
        try:
            variables[word] += int(lines[iter][2])
        except:
            variables[word] += int(variables[lines[iter][2]])
        iter += 1

    elif lines[iter][0] == "SUB":   #If command is sub
        word = lines[iter][1]
        try:
            variables[word] -= int(lines[iter][2])
        except:
            variables[word] -= int(variables[lines[iter][2]])
        iter += 1

    elif lines[iter][0] == "HALT":  #If command is halt
        quit()

    else:
        print(lines[iter][0])
        print("Invalid command entered")
        quit()