#I am taking inputs from the user
glass_size = int(input())
stra_pos = int(input())

#I am making some copies of the variables to use them later
glass_size_copyF = glass_size

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
    """starts with printing "o"s for the first stra_pos lines
        Since this pattern is same for each picture
        I place it at the beginning of the code"""

    for ff in range(stra_pos):
        for c in range(ff):
            print(" ", end='')
        print("o")

    """preSpace is the variable that determines the number of " " preceding chars
    Since it should be changed in the loop I created it outside of the loop """
    preSpace = 0

    """This loop prints lines that include both the glass and a part of the straw
    For example: '\  0/'
       """

    #excetued i times before in each picture we have different number of straw length
    for b in range(i):
        #printing pre-spaces for in-glass straw parts
        for k in range(preSpace):
            print(" ", end='')
        print("\\", end='')
        #printing the inside spaces that are after \ char
        for j in range(stra_pos + b - preSpace - 1):
            print(" ", end='')
        #when all space locations are done, program just prints the straw part on that line
        print("o", end='')

        #After printing o we may need some other spaces before printing '/'
        afterSpace = 2 * glass_size_copyF - stra_pos
        for h in range(afterSpace):
            print(" ", end='')
        print("/")
        #preSpace is incremented by one because in each row the space that preceds the line increments one
        preSpace += 1
        glass_size_copyF -= 1

    glass_size_copyF = glass_size



    for c in range(glass_size - i):
        for j in range(preSpace):
            print(" ", end = '')
        print("\\", end = '')

        for h in range(2 * (glass_size - i - c)):
            print("*", end = '')
        print("/")
        preSpace += 1

    #prints the common part whose lines include neither * nor o char, but only || and --
    #before printing "--" we still need some spaces whose number is determined by constant_preSpace, look line: 22
    for h in range(constant_preSpace):
        print(" ", end='')
        #we need 2 '-' char, we may write it with loop/not sure about its neccesity mail to TAs.
        for k in range(2):
            print("-")
    for h in range(glass_size):
        # before printing "|" we still need some spaces whose number is determined by constant_preSpace, look line: 22
        for z in range(constant_preSpace):
            print(" ", end='')
            # we need 2 '|' char, we may write it with loop
            for j in range(2):
                print("|")
    #to have a one empty line between 2 pictures at the end I use print()
    print()
