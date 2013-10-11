mess = open('mess03.txt')

for line in mess:
    for i in range(len(line)-9):
        if line[i].islower()==True and line[i+1:i+4].isupper()==True and line[i+4].islower()==True and line[i+5:i+8].isupper()==True and line[i+8].islower()==True:
            print (line[i:i+9])

print("Done")
