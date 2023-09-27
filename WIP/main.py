"""
bool = True
wrong_count = 0
wrong_array = []
wrong_array_lcm = []
num_range = 100000
for x in range(1,num_range):
    test = float(1 / x)
    print("x = ", x, ": ", float(x) * test)
    if (float(x) * test) != 1:
        bool = False
        wrong_count += 1
        wrong_array.append(x)
print(bool)
print(wrong_count, " wrong(", float(100.0 * wrong_count / num_range), "% incorrect)")
wrong_array_lcm.append(wrong_array[0])
i = 1
while i < len(wrong_array):
    new = True
    for x in wrong_array_lcm:
        if wrong_array[i] % x == 0:
            new = False
    if new:
        wrong_array_lcm.append(wrong_array[i])
    i += 1

print("Wrong LCM: ", wrong_array_lcm)



a = 1
b = "/"
c = 3
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(str(arr[0][0]), "/", str(arr[2][2]))

rotor_I = ['J', 'G', 'D', 'Q', 'O', 'X', 'U', 'S', 'C', 'A', 'M', 'I', 'F', 'R', 'V', 'T', 'P', 'N', 'E', 'W', 'K', 'B',
           'L', 'Z', 'Y', 'H']


def test(rotor, cha):
    return chr(rotor.index(cha)+65)


print(test(rotor_I, 'H'))
"""
string = "hell"
last = 'o'

print(string.count('z'))