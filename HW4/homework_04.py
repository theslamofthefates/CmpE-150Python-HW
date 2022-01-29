# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


"""
    1- I made variable naming as clear as possible; therefore, I may not explain what each of them does.
    2- I separated operations by comments to make it easier to read/ follow.
"""

"""
    //////////////////////////////
    START OF OPERATION 1    
    //////////////////////////////
"""


def operation_1(file_name):
    new_min = int(input())
    new_max = int(input())
    img, old_max = read_ppm_file(file_name)
    old_min = 0  # by default
    for line in range(len(img)):  # each row
        for pixel in range(len(img[line])):
            for channel in range(len(img[line][pixel])):
                temp = round(
                    ((img[line][pixel][channel] - old_min) / (old_max - old_min) * (new_max - new_min) + new_min), 4)
                img[line][pixel][channel] = temp  # updating the channel value
    return img


"""
    //////////////////////////////
    END OF OPERATION 1    
    //////////////////////////////
    START OF OPERATION 2
    //////////////////////////////
"""


def operation_2_mean(channel):  # Function to calc. mean of a list
    ans = 0
    for b in channel:
        ans += b
    return ans / len(channel)


def operation_2_stDev(channel):  # Function to calc. st. deviation of a list
    ans = 0
    mean = operation_2_mean(channel)
    for b in channel:
        ans += (b - mean) ** 2
    return (ans / len(channel)) ** 0.5 + 1e-6


def generate_channels(img):  # function that takes a img and creates a different list for each channel
    channel_r = []  # stands for Red
    channel_g = []  # stands for green
    channel_b = []  # stands for blue
    for line in img:
        for pixel in line:
            channel_r.append(pixel[0])
            channel_g.append(pixel[1])
            channel_b.append(pixel[2])
    return channel_r, channel_g, channel_b


def operation_2(file_name):
    img = read_ppm_file(file_name)[0]
    channel_r, channel_g, channel_b = generate_channels(img)
    mean_r = operation_2_mean(channel_r)  # mean val. of Red
    mean_g = operation_2_mean(channel_g)  # mean val. of green
    mean_b = operation_2_mean(channel_b)  # mean val. of blue
    stdDev_r = operation_2_stDev(channel_r)  # std. dev. of Red
    stdDev_g = operation_2_stDev(channel_g)  # std. dev. of green
    stdDev_b = operation_2_stDev(channel_b)  # std. dev. of blue
    for row in img:
        for pixel in row:
            # updating the each channel val.
            pixel[0] = round((pixel[0] - mean_r) / (stdDev_r), 4)
            pixel[1] = round((pixel[1] - mean_g) / (stdDev_g), 4)
            pixel[2] = round((pixel[2] - mean_b) / (stdDev_b), 4)
    return img


"""
    //////////////////////////////
    END OF OPERATION 2    
    //////////////////////////////
    START OF OPERATION 3
    //////////////////////////////
"""


def pixel_mean(pixel):  # mean val. of a pixel
    ans = 0
    for k in pixel:
        ans += k
    return int(ans / 3)


def operation_3(file_name):
    img = read_ppm_file(file_name)[0]
    for line in img:
        for pixel in line:
            pixel_m = pixel_mean(pixel)  # created a variable to reduce the number of call for pixel_mean() function
            for c in range(3):  # c -> channel
                pixel[c] = pixel_m  # updating each value
    return img


"""
    //////////////////////////////
    END OF OPERATION 3   
    //////////////////////////////
    START OF OPERATION 4
    //////////////////////////////
"""


def get_convolution_matrix(filter_name):  # takes a file name and returns a nested list of the filter
    with open(filter_name) as file:
        convolution_matrix = file.readlines()
    for b in range(len(convolution_matrix)):
        convolution_matrix[b] = convolution_matrix[b].rstrip()  # remove "\n"
        convolution_matrix[b] = convolution_matrix[b].split()
        for c in range(len(convolution_matrix[b])):
            convolution_matrix[b][c] = float(convolution_matrix[b][c])
    return convolution_matrix


def get_new_value(filter_matrix, _x, _y, img, color):  # returns the new value of a given coord. (_x, _y)
    # and a filter_matrix and img. color indicates the channel
    size_x = len(filter_matrix)
    size_y = len(filter_matrix[0])
    output = 0
    row = 0  # row and col is used to get coefficients from filter_matrix, these are corresponding coordinates
    for b in range(_x - size_x // 2, _x + size_x // 2 + 1):
        col = 0
        for c in range(_y - size_y // 2, _y + size_y // 2 + 1):
            output += img[b][c][color] * filter_matrix[row][col]  # multiply the overlapping parts of two list
            col += 1
        row += 1
    if output < 0:
        return 0
    elif output > 255:
        return 255
    return int(output)


def operation_4(file_name, filter_name, stride):
    if type(file_name) != list:
        img = read_ppm_file(file_name)[0]
    else:
        img = file_name  # this part is for operation 5
    filter_matrix = get_convolution_matrix(filter_name)  # explained above
    padding = (len(filter_matrix) - 1) // 2  # I created this variable because where we start to apply the filter
    # depends on the size of the filter
    general = []
    for line in range(padding, len(img) - padding, stride):
        row = []  # each new row
        for pixel in range(padding, len(img[line]) - padding, stride):
            res_pixel = []  # each new pixel
            for color in range(3):  # range(3) because get_new_value requires the channel code, 0-1-2
                res_pixel.append(get_new_value(filter_matrix, line, pixel, img, color))
            row.append(res_pixel)
        general.append(row)
    return general


"""
    //////////////////////////////
    END OF OPERATION 4   
    //////////////////////////////
    START OF OPERATION 5
    NOTES: Some functions of OP4 are used here as well. look line 195
    //////////////////////////////
"""


def operation_5(file_name, filter_name, stride):
    img = read_ppm_file(file_name)[0]
    filter_matrix = get_convolution_matrix(filter_name)
    padding = (len(filter_matrix) - 1) // 2
    ss_main = []
    empty_slot = []
    for b in range(len(img) + 2 * padding):  # create an empty row -> [0, 0, 0]
        empty_slot.append([0, 0, 0])
    for c in range(padding):
        ss_main.append(empty_slot)
    for k in range(len(img)):
        temp_line = []  # each new row
        empty_ss = [0, 0, 0]
        for z in range(padding):
            temp_line.append(empty_ss)
        for cc in range(len(img[0])):  # adding elements
            temp_line.append(img[k][cc])
        for z in range(padding):
            temp_line.append(empty_ss)
        ss_main.append(temp_line)  # adding this row to the main list
    for c in range(padding):
        ss_main.append(empty_slot)
    return operation_4(ss_main, filter_name, stride)  # I use the same function with operation-4


"""
    //////////////////////////////
    END OF OPERATION 5  
    //////////////////////////////
    START OF OPERATION 6
    //////////////////////////////
"""


def check_pixels(pixel_1, pixel_2, ran):  # checking two pixels whether all channels' difference is less than ran
    for b in range(3):
        if abs(pixel_2[b] - pixel_1[b]) >= ran:
            return False
    return True


def operation_6_solver(main_img, generated_img, ran, _x=0, _y=0, controller=0):
    """
    :param main_img: list -> all changes are done on that list
    :param generated_img: list -> determines the direction of the move
        if this list == ['s', 's', 's'] this means any operations aren't done on that pixel yet. So move into that
        direction.
        elif this list == ['a', 'a', 'a'] this means a operation has already done on that pixel.

    :param ran: int -> range of difference
    :param _x: int -> x coordinate of the current pixel
    :param _y: int -> y coordinate of the current pixel
    :param controller: int -> checks if all pixels are visited
    :return: list -> resulting image
    """
    if controller == len(main_img) ** 2 - 1:  # when all pixels are visited stop the recursive call
        img_printer(main_img)
        return

    # first try to move down
    if 0 <= _x < len(main_img) - 1 and 0 <= _y < len(main_img) - 1 and generated_img[_y + 1][_x] == ['s', 's', 's']:
        if check_pixels(main_img[_y][_x], main_img[_y + 1][_x], ran):
            for b in range(3):
                main_img[_y + 1][_x][b] = main_img[_y][_x][b]
        else:
            for b in range(3):
                main_img[_y][_x][b] = main_img[_y][_x][b]
        generated_img[_y + 1][_x] = ['a', 'a', 'a']  # since an operation is done, change the list
        generated_img[_y][_x] = ['a', 'a', 'a']  # since an operation is done, change the list
        return operation_6_solver(main_img, generated_img, ran, _x, _y + 1, controller + 1)

    # then try to move up
    elif 0 <= _x < len(main_img) and 0 < _y < len(main_img) and generated_img[_y - 1][_x] == ['s', 's', 's']:
        if check_pixels(main_img[_y - 1][_x], main_img[_y][_x], ran):  # if check_pixel returns True
            for b in range(3):
                main_img[_y - 1][_x][b] = main_img[_y][_x][b]   # make these two pixel equal
        else:
            for b in range(3):
                main_img[_y][_x][b] = main_img[_y][_x][b]
        generated_img[_y - 1][_x] = ['a', 'a', 'a']  # since an operation is done, change the list
        generated_img[_y][_x] = ['a', 'a', 'a']  # since an operation is done, change the list
        return operation_6_solver(main_img, generated_img, ran, _x, _y - 1, controller + 1)  # move 1 pixel to right

    # then try to move right
    elif 0 <= _x < len(main_img) and 0 <= _y <= len(main_img) - 1 and generated_img[_y][_x + 1] == ['s', 's', 's']:
        if check_pixels(main_img[_y][_x], main_img[_y][_x + 1], ran):
            for b in range(3):
                main_img[_y][_x + 1][b] = main_img[_y][_x][b]
        else:
            for b in range(3):
                main_img[_y][_x][b] = main_img[_y][_x][b]
        generated_img[_y][_x + 1] = ['a', 'a', 'a']  # since an operation is done, change the list
        generated_img[_y][_x] = ['a', 'a', 'a']  # since an operation is done, change the list
        return operation_6_solver(main_img, generated_img, ran, _x + 1, _y, controller + 1)


"""
    //////////////////////////////
    END OF OPERATION 6
    //////////////////////////////
    START OF OPERATION 7
    //////////////////////////////
"""


def operation_7_solver(main_img, generated_img, ran, cur_channel=0, _x=0, _y=0, controller=0):
    """
    Similar to operation_6
    :param main_img: list -> all changes are done on that list
    :param generated_img: list -> determines the direction of the move
        if generated_img[][][cur_channel] == ['s'] this means any operations aren't done on that pixel yet. So move into that
        direction.
        elif this list == ['a'] this means a operation has already done on that pixel.

    :param ran: int -> range of difference
    :param cur_channel: indicates 0 -> r, 1 -> g, 2 -> b
    :param _x: int -> x coordinate of the current pixel
    :param _y: int -> y coordinate of the current pixel
    :param controller: int -> checks if all pixels are visited
    :return: list -> resulting image
    """

    if controller == (len(main_img) ** 2) * 3 - 1:  # checks if all possible destinations are visited
        img_printer(main_img)
        return

    if 0 <= _x < len(main_img) and 0 <= _y < len(main_img) - 1 and generated_img[_y + 1][_x][
        cur_channel] == 's':  # try down
        if abs(main_img[_y][_x][cur_channel] - main_img[_y + 1][_x][cur_channel]) < ran:
            main_img[_y + 1][_x][cur_channel] = main_img[_y][_x][cur_channel]
        else:
            main_img[_y][_x][cur_channel] = main_img[_y][_x][cur_channel]
        generated_img[_y + 1][_x][cur_channel] = 'a'  # since an operation is done, change the list
        generated_img[_y][_x][cur_channel] = 'a'  # since an operation is done, change the list
        return operation_7_solver(main_img, generated_img, ran, cur_channel, _x, _y + 1, controller + 1)

    elif 0 <= _x < len(main_img) and 0 < _y < len(main_img) and generated_img[_y - 1][_x][cur_channel] == 's':  # try up
        if abs(main_img[_y - 1][_x][cur_channel] - main_img[_y][_x][cur_channel]) < ran:
            main_img[_y - 1][_x][cur_channel] = main_img[_y][_x][cur_channel]
        else:
            main_img[_y][_x][cur_channel] = main_img[_y][_x][cur_channel]
        generated_img[_y - 1][_x][cur_channel] = 'a'  # since an operation is done, change the list
        generated_img[_y][_x][cur_channel] = 'a'  # since an operation is done, change the list
        return operation_7_solver(main_img, generated_img, ran, cur_channel, _x, _y - 1, controller + 1)

    elif 0 <= _x < len(main_img) - 1 and 0 <= _y <= len(main_img) - 1 and generated_img[_y][_x + 1][
        cur_channel] == 's':  # try right
        if abs(main_img[_y][_x][cur_channel] - main_img[_y][_x + 1][cur_channel]) < ran:
            main_img[_y][_x + 1][cur_channel] = main_img[_y][_x][cur_channel]
        else:
            main_img[_y][_x][cur_channel] = main_img[_y][_x][cur_channel]
        generated_img[_y][_x + 1][cur_channel] = 'a'  # since an operation is done, change the list
        generated_img[_y][_x][cur_channel] = 'a'  # since an operation is done, change the list
        return operation_7_solver(main_img, generated_img, ran, cur_channel, _x + 1, _y, controller + 1)

    elif 0 <= _x < len(main_img) and 0 <= _y < len(main_img) and generated_img[_y][_x - 1][
        cur_channel] == 's':  # try left
        if abs(main_img[_y][_x][cur_channel] - main_img[_y][_x - 1][cur_channel]) < ran:
            main_img[_y][_x - 1][cur_channel] = main_img[_y][_x][cur_channel]
        else:
            main_img[_y][_x][cur_channel] = main_img[_y][_x][cur_channel]
        generated_img[_y][_x - 1][cur_channel] = 'a'  # since an operation is done, change the list
        generated_img[_y][_x][cur_channel] = 'a'  # since an operation is done, change the list
        return operation_7_solver(main_img, generated_img, ran, cur_channel, _x - 1, _y, controller + 1)

    elif _x == len(main_img) - 1 or _x == 0 and _y == 0 or _y == len(main_img) - 1 and generated_img[_y][_x][
        cur_channel + 1] == 's' and cur_channel < 3:  # try increment current_channel
        if abs(main_img[_y][_x][cur_channel] - main_img[_y][_x][cur_channel + 1]) < ran:
            main_img[_y][_x][cur_channel + 1] = main_img[_y][_x][cur_channel]
        else:
            main_img[_y][_x][cur_channel] = main_img[_y][_x][cur_channel]
        generated_img[_y][_x][cur_channel] = 'a'  # since an operation is done, change the list
        generated_img[_y][_x][cur_channel + 1] = 'a'  # since an operation is done, change the list
        return operation_7_solver(main_img, generated_img, ran, cur_channel + 1, _x, _y, controller + 1)


"""
    //////////////////////////////
    END OF OPERATION 7
    //////////////////////////////
    START OF MAIN Function
    //////////////////////////////
"""


def main():
    if operation == 1:
        img_printer(operation_1(filename))

    elif operation == 2:
        img_printer(operation_2(filename))

    elif operation == 3:
        img_printer(operation_3(filename))

    elif operation == 4:
        filter_name = input()
        stride = int(input())
        img_printer(operation_4(filename, filter_name, stride))

    elif operation == 5:
        filter_name = input()
        stride = int(input())
        img_printer(operation_5(filename, filter_name, stride))

    elif operation == 6:
        ran = int(input())
        img = read_ppm_file(filename)[0]
        generated_img = []

        # creating empty list
        for b in range(len(img)):
            temp = []
            for c in range(len(img[0])):
                pixel = []
                for k in range(3):
                    pixel.append('s')
                temp.append(pixel)
            generated_img.append(temp)

        generated_img[0][0] = ['a', 'a', 'a']   # first pixel is initially done
        operation_6_solver(img, generated_img, ran)

    elif operation == 7:
        ran = int(input())
        img = read_ppm_file(filename)[0]
        generated_img = []

        # creating empty list
        for b in range(len(img)):
            temp = []
            for c in range(len(img[0])):
                pixel = []
                for k in range(3):
                    pixel.append('s')
                temp.append(pixel)
            generated_img.append(temp)

        generated_img[0][0] = ['a', 's', 's']   # first channel is initially done
        operation_7_solver(img, generated_img, ran)


# main call


main()

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
