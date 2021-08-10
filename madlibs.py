import sys

def get_word():
    return input('Enter a word: ')

def parse_args(args:
    ret = []
    for arg in args[1:]:
        ret.append(arg)
    return ret

args = parse_args(sys.argv)
for index in range(len(sys.argv)):
    if args[index] == '_':
        args[index] = get_word()v


sys.argv.pop(0)
result = ' '.join(args)

print(result)
print(args)
print(sys.argv)
