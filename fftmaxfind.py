#For finding maximums among violin bow data ffts


filename = "022813.run6.p5.3,45-3,55.r.dat.fft.txt"
top = "1000"
outputname = filename[:len(filename)-4]+".max.txt"
#filename = input("What is the name of the file?\n")
#top = input("What is the maximum x value that should be searched?\n")
#outputname = ""
#while outputname==filename or outputname=="":
#    outputname = input("Enter a name for an output file:\n")


data = open(filename)
output = open(outputname, 'w')

maxlines = []

firstline = data.readline()
b = eval(firstline[8:])
pastline = data.readline()
c = eval(pastline[8:])

i=2
for line in data:
    a = b
    b = c
    c = eval(line[8:])
    if b>a and b>c:
        output.write(pastline)
    pastline = line
    i += 1
    if eval(line[:len(top)])>eval(top):
        break

data.close()
output.close()
