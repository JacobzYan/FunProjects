dice_type = []
dice_count = []
responses = ["y", "n", "yes", "no"]
total = 0
roll_count = 0
more_dice = True


while more_dice:
    dice_type.append(int(input("How many faces on this die?\n")))
    dice_count.append((int(input("How many of these dice?\n"))))
    invalid_input = True
    while invalid_input:
        temp = str(input("Would you like to add more dice? y/n\n"))
        temp.lower()
        print(temp)
        stupid = False
        if responses.count(temp) != 0:
            print("goodresponse")
        else:
            stupid = True
        print("stupid: ", stupid)
        if stupid:
            print("Invalid input, please try again (Valid inputs include y, n, yes, and no)")
        else:
            invalid_input = False
            if temp == 'n':
                more_dice = False
print("output:")
index = 0
while index != len(dice_type):
    temp_list = []
    temp_list.append(dice_count[index])
    temp_list.append("d")
    temp_list.append(dice_type[index])
    str = "".join([str(x) for x in temp_list])
    print(str)
    index += 1




