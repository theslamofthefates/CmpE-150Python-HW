#I am taking inputs from the user
glass_size = int(input())
stra_pos = int(input())

#I am making some copies of the variables to use them later
glass_size_copyF = glass_size
stra_pos_copyF = stra_pos

#number_of_shots will be the number of pictures
number_of_shots = 0

#To obtain number of shots, I use a logical conclusion
f = glass_size * 2 - stra_pos + 1
if f % 2 == 0:
    #Since it is even no need to add 1, integer division is required because later I'll use this variable in a loop
    number_of_shots = f // 2
else:
    # Since it is odd adding 1 is necessary, integer division is required because later I'll use this variable in a loop
    number_of_shots = (f + 1)//2

#constant_preSpace, as its name indicates, holds the number of preSpace characters in some lines
constant_preSpace = glass_size

for i in range(number_of_shots + 1):
    #starts with printing "o"s for the first stra_pos lines
    for ff in range(stra_pos):
        for c in range(ff):
            print(" ", end='')
        print("o")

    #prints the insertion
    preSpace = 0
    for b in range(i):
        for k in range(preSpace):
            print(" ", end='')
        print("\\", end='')
        for j in range(stra_pos + b - preSpace - 1):
            print(" ", end='')
        print("o", end='')


        afterSpace = 2 * glass_size_copyF - stra_pos
        for h in range(afterSpace):
            print(" ", end='')
        print("/")
        preSpace += 1
        glass_size_copyF -= 1
        stra_pos_copyF += 1

    glass_size_copyF = glass_size
    stra_pos_copyF = stra_pos

    #prints the rest of the code
    for c in range(glass_size - i):
        for j in range(preSpace):
            print(" ", end = '')
        print("\\", end = '')

        for h in range(2 * (glass_size - i - c)):
            print("*", end = '')
        print("/")
        preSpace += 1
    for h in range(constant_preSpace):
        print(" ", end='')
    print("--")
    for h in range(glass_size):
        for z in range(constant_preSpace):
            print(" ", end='')
        print("||")
    print()
