mess = open('mess02.txt')

chars = []

for line in mess:
    for i in range(len(line)):
        new=True
        for j in range(len(chars)):
            if line[i]==chars[j][0]:
                new=False
                chars[j][1] += 1
        if new==True:
            chars.append([line[i],1])
                
            

print(chars)
