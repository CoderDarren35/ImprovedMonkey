import sys

n = int(sys.argv[1])

if n % 2 == 1:

    print("weird")

elif n >= 2 and n <= 5:

    print("not weird")

elif n >= 6 and n <=  20:

    print("Weird")

elif n >= 20:

    print("not weird")

#x % y = remainder(x/y) 
