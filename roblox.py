import sys

arg = sys.argv[1]

character = arg[0]

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:',  str(sys.argv))

print(arg)
print(character)

if character == "1":   
    print("one")
else:
    print("not a one")

print(character)
