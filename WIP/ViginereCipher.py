# Setup
# need to figure out char to int
def encode_char(plaintext, keyphrase):
    key_index = 0
    max_index = keyphrase.length()
    for i in plaintext:
        print("no")

test = 'A'


running = True
print("input \"H\" or \"Help\" for commands")
while running:
    navigation = str(input("Viginere Interface Awaiting Input: ").upper())

    # Function selection
    if navigation == "E" or navigation == "ENCODE":
        print("Encoding")

    elif navigation == "D" or navigation == "DECODE":
        print("Decoding")

    elif navigation == "K" or navigation == "KEY":
        print("Key")

    elif navigation == "H" or navigation == "HELP":
        print("Available Commands:")
        print("Input \"E\" or \"Encode\" to encode a message")
        print("Input \"D\" or \"Input\" to decode a message")
        print("Input \"K\" or \"key\" to change the keyphrase")
        print("Input \"X\" or \"Exit\" to terminate the program")

    elif navigation == "X" or navigation == "END":
        running = False
        print("Program Exiting")

    else:
        print("Invalid input, please try again")
