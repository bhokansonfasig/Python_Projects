decoded = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

coded = ['y','z','a','b','c','d','e','f','g','h','i','j','k',
         'l','m','n','o','p','q','r','s','t','u','v','w','x']


if len(decoded)!=len(coded):
    print("Error: Not each character has a character to map to.\nSuggested to close the program and fix the issue.\n")

message = input("Coded message:")

message.lower()

marray = []
oarray = []

for i in range(len(message)):
    marray.append(message[i])

for i in range(len(marray)):
    changed = False
    for j in range(len(decoded)):
        if marray[i]==coded[j]:
            oarray.append(decoded[j])
            changed = True
            break
    if changed==False:
        oarray.append(marray[i])

output = ""

for i in range(len(oarray)):
    output = output + oarray[i]

print()
print(output)

#When given error 'int object not iterable', make sure your for loops
#   include range(len(..)) not just len(..)
