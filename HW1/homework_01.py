
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# I am making some copies of the variables to use them later
glass_size_copyF = glass_size
straw_pos_copy = straw_pos

# number_of_shots will be the number of pictures
number_of_shots = 0

# To obtain number of shots, I use a logical conclusion
f = glass_size * 2 - straw_pos + 1
if f % 2 == 0:
    # Since it is even no need to add 1, integer division is required because later I'll use this variable in a loop
    number_of_shots = f // 2
else:
    # Since it is odd adding 1 is necessary, integer division is required because later I'll use this variable in a loop
    number_of_shots = (f + 1)//2

# constant_preSpace, as its name indicates, holds the number of preSpace characters in some lines
constant_preSpace = glass_size

for i in range(number_of_shots + 1):
    """starts with printing "o"s for the first straw_pos lines
        Since this pattern is same for each picture
        I place it at the beginning of the code"""

    for ff in range(straw_pos):
        for c in range(ff):
            print(" ", end='')
        print("o")

    """preSpace is the variable that determines the number of " " preceding chars
    Since it should be changed in the loop I created it outside of the loop """
    preSpace = 0

    """This loop prints lines that include both the glass and a part of the straw
    For example: '\  0/'
       """

    # executed times before in each picture we have different number of straw length
    for b in range(i):
        # printing pre-spaces for in-glass straw parts
        for k in range(preSpace):
            print(" ", end='')
        print("\\", end='')
        # printing the inside spaces that are after \ char
        for j in range(straw_pos + b - preSpace - 1):
            print(" ", end='')
        # when all space locations are done, program just prints the straw part on that line
        print("o", end='')

        # After printing o we may need some other spaces before printing /
        afterSpace = 2 * glass_size_copyF - straw_pos
        for h in range(afterSpace):
            print(" ", end='')
        print("/")
        # preSpace is incremented by one because in each row the space that precedes the line increments one
        preSpace += 1
        glass_size_copyF -= 1
        straw_pos_copy += 1

    glass_size_copyF = glass_size
    straw_pos_copyF = straw_pos


    for c in range(glass_size - i):
        for j in range(preSpace):
            print(" ", end='')
        print("\\", end='')

        for h in range(2 * (glass_size - i - c)):
            print("*", end='')
        print("/")
        preSpace += 1

    # prints the common part whose lines include neither * nor o char, but only || and --
    # before printing "--" we still need some spaces whose number is determined by constant_preSpace, look line: 22
    for h in range(constant_preSpace):
        print(" ", end='')
    # we need 2 '-' char, so created a range in 2
    for oo in range(2):
        print("-", end="")
    print()
    for h in range(glass_size):
        # before printing "|" we still need some spaces whose number is determined by constant_preSpace, look line: 22
        for z in range(constant_preSpace):
            print(" ", end='')
        # we need 2 '|' char, so created a range in 2
        for j in range(2):
            print("|", end="")
        print()
    # to have a one empty line between 2 pictures at the end I use print()


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


