import random

def is_sorted(list):
    # Set up needed variables
    flag = True
    compare_to = -1

    # Loop through list and compare to previous
    for i in list:
        if(i < compare_to):
            flag = False
            break
        else:
            compare_to = i
    return flag


# Set up random list
list_length = int(input("Enter a list length:\n"))
random.seed()
bogo_list = []

# Randomly fill list
for a in range(list_length):
    bogo_list.append(random.randrange(1, max(list_length + 10, 100), 1))

# Set up variables for sorting attempts
tries = 0
wrong = True

# Loop through attempts while printing
print(bogo_list)
while wrong:
    
    # Check if correct else add 1 to counter
    if is_sorted(bogo_list):
        break
    
    tries += 1

    # Randomize list
    temp_list = []
    current_index = 0
    while current_index < list_length:

        temp_list.append(bogo_list.pop(random.randrange(0, list_length - current_index, 1)))
        current_index += 1
    
    # Reassign shuffled list to normal, print
    bogo_list = temp_list
    print('Attempt ',tries, ": ",bogo_list)
    
print("Randomizes taken = ", tries)
