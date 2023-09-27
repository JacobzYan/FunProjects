# uses Enigma I, rotors 1, 2, 3
positions = [1, 1, 1]
ring_positions = [1, 1, 1]
rotor_I = ['J', 'G', 'D', 'Q', 'O', 'X', 'U', 'S', 'C', 'A', 'M', 'I', 'F', 'R', 'V', 'T', 'P', 'N', 'E', 'W', 'K', 'B',
           'L', 'Z', 'Y', 'H']
rotor_II = ['N', 'T', 'Z', 'P', 'S', 'F', 'B', 'O', 'K', 'M', 'W', 'R', 'C', 'J', 'D', 'I', 'V', 'L', 'A', 'E', 'Y',
            'U', 'X', 'H', 'G', 'Q']
rotor_III = ['J', 'V', 'I', 'U', 'B', 'H', 'T', 'C', 'D', 'Y', 'A', 'K', 'E', 'Q', 'Z', 'P', 'O', 'S', 'G', 'X', 'N',
             'R', 'M', 'W', 'F', 'L']
reflector_A = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P',
               'I', 'K', 'H', 'G', 'D']
plugboard = []
running = True


# TO DO
# IMPROVE STATUS MESSAGES
# ADD IN OTHER ROTORS, MAKE IT POSSIBLE TO SWITCH ROTORS
def cycle_rotors():
    if positions[0] == 26:
        positions[0] = 1
        if positions[1] == 26:
            positions[1] = 1
            if positions[2] == 26:
                positions[2] = 1
            else:
                positions[2] += 1
        else:
            positions[1] += 1
    else:
        positions[0] += 1


def through_rotor(rotor, cha, rotor_location):
    return rotor[(ord(cha.upper()) - 65 + positions[rotor_location-1] - 1) % 26]


def through_inverse(rotor, cha, rotor_location):
    return chr((rotor.index(cha.upper()) - positions[rotor_location - 1] + 1) % 26 + 65)


def encode_char(inp):
    cycle_rotors()
    temp = []
    for a in inp:
        temp_char = a
        for b in plugboard:
            if a == b[0]:
                temp_char = b[1]
            elif a == b[1]:
                temp_char = b[0]
        temp.append(temp_char)

    temp = inp
    temp = through_rotor(rotor_I, temp, 1)
    temp = through_rotor(rotor_II, temp, 2)
    temp = through_rotor(rotor_III, temp, 3)
    temp = reflector_A[(ord(temp) - 65) % 26]
    temp = through_inverse(rotor_III, temp, 3)
    temp = through_inverse(rotor_II, temp, 2)
    temp = through_inverse(rotor_I, temp, 1)

    return temp


print("input \"H\" or \"Help\" for commands")
disp_status = True
while running:

    if disp_status:
        temp_navigation = input("Enigma Interface Awaiting Input: ")
    else:
        temp_navigation = input("")

    disp_status = True

    navigation = str(temp_navigation.upper())

    if navigation == "T" or navigation == "TEST":
        testing = True
        while testing:
            temporary = input("Enter a char to go through rotor 1, n to exit")
            if temporary == 'n':
                testing = False
            else:
                print(through_rotor(rotor_I, temporary, 1))
                print("reversed: ", through_inverse(rotor_I, temporary, 1))
        """
        for x in positions:
            print(x, end='')
        print('')
        print(navigation)
        for x in rotor_I:
            print(x, end='')
        print('')
        for x in rotor_II:
            print(x, end='')
        print('')
        for x in rotor_III:
            print(x, end='')
        print('')
        for x in reflector_A:
            print(x, end='')

        print("\n Setting rotor values to  test overflow")
        positions = [25, 1, 1]
        for x in "aaa":
            nothing = x
            print(positions)
            cycle_rotors()
        print("")

        positions = [25, 26, 1]
        for y in "aaa":
            print(positions)
            cycle_rotors()
        print("")

        positions = [25, 26, 26]
        for z in "aaa":
            print(positions)
            cycle_rotors()
        print("")
        print("\nTesting sending through rotors")
        print(through_rotor(rotor_I, 'D'))
        print(through_inverse(rotor_I, 'C'))
        """

    elif navigation == "R" or navigation == "ROTORS":
        sub_running = True
        print("Now editing rotors")
        print("Current rotor configuration: ")
        print("Rotor I: ", positions[0], "\nRotor II:", positions[1], "\nRotor III:", positions[2])
        while sub_running:
            rotor_to_edit = int(input("Select rotor to edit(1-3): "))
            new_rotor_number = int(input("Enter new number for rotor(1-26): "))
            if 1 <= rotor_to_edit <= 3 and 1 <= new_rotor_number <= 26:
                positions[(rotor_to_edit - 1)] = new_rotor_number
                print("New rotor configuration: ")
                print("Rotor I: ", positions[0], "\nRotor II:", positions[1], "\nRotor III:", positions[2])
                change_other = input("Edit another Rotor?(Y/N)")
                if change_other.upper() == "N":
                    sub_running = False
            else:
                print("invalid input, please try again")

    elif navigation == "P" or navigation == "PLUGBOARD":

        # Information
        print("Input a pair of characters to connect them on the plugboard. ",
              "Input an existing pair to delete it; input e to exit")
        print("Existing connections:")
        if len(plugboard) == 0:
            print("None")
        else:
            for x in plugboard:
                print(x)

        # Checking, Processing Input
        inputting = True
        while inputting:
            raw_input = input("Awaiting input:")
            input_good = True
            processed_input = []
            exists_already = False
            # Check for exit command
            if raw_input.upper() == 'E':
                inputting = False
                break
            # Check Length = 2
            if len(str(raw_input)) != 2:
                input_good = False
            # Check they are letters
            for x in raw_input:
                if ord(x.upper()) < 65 or ord(x.upper()) > 90:
                    input_good = False
            # Check they are different
            if raw_input[0] == raw_input[1]:
                input_good = False
            # Check alphabetical order, flip if needed
            if ord(raw_input[0]) < ord(raw_input[1]):
                processed_input.append(raw_input[0].upper())
                processed_input.append(raw_input[1].upper())
            else:
                processed_input.append(raw_input[1].upper())
                processed_input.append(raw_input[0].upper())
            # See if need to add or delete
            for x in plugboard:
                if x == processed_input:
                    exists_already = True
            if exists_already:
                plugboard.remove(processed_input)
                print("Connection ", processed_input, " removed")
            else:
                # Make sure letters not being used by other connection
                for x in processed_input:
                    for y in plugboard:
                        if x == y[0] or x == y[1]:
                            input_good = False
                if input_good:
                    plugboard.append(processed_input)
                    continue_input = input("Add another connection?(Y/N): ")
                    if continue_input.upper() != 'Y':
                        inputting = False
                else:
                    print("Invalid input, please try again")

    elif navigation == "E" or navigation == "END":
        print("Program Exiting")
        running = False

    elif navigation == "H" or navigation == "HELP":
        print("Available Commands:")
        print("Input \"R\" or \"Rotors\" to edit rotor starting position")
        print("Input \"I\" or \"Input\" to input a message")
        print("Input \"P\" or \"PLUGBOARD\" to swap letters")
        print("Input \"E\" or \"End\" to terminate the program")

    # Default to message Input
    else:
        # elif navigation == "I" or navigation == "INPUT":

        # Processing Plaintext
        # raw_plaintext = str(input("Enter Message(spaces will be deleted):\n"))
        # plaintext = str('')
        # for char in raw_plaintext:
        #     if 65 <= ord(char.upper()) <= 90:
        #         plaintext = plaintext + char.upper()
        if navigation == 'I':
            plaintext = str(input("Enter Message:\n"))
        else:
            plaintext = temp_navigation
        # Encoding
        ciphertext = ""
        for character in plaintext:
            if 65 <= ord(character.upper()) <= 90:
                ciphertext = ciphertext + encode_char(character)
                # (encode_char(char))
            else:
                ciphertext = ciphertext + character
        print("\n", ciphertext)
        disp_status = False
