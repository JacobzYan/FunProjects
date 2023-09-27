# Start with Integer N, if n is even, divide it by 2, if N is odd, multiply by 3, add 1


Still_going = True
while Still_going:
    step_count = 0
    n = int(input("Enter Starting number: "))
    current_number = n

    while current_number != 1:
        print(int(current_number))
        if current_number % 2 == 1:
            current_number = 1 + 3 * current_number
        else:
            current_number = current_number / 2
        step_count = step_count + 1
    print(int(current_number))
    print("Steps taken:", step_count)

    Still_going = input("Calculate again?: ").upper() != "N"
