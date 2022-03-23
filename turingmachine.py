data_input = [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]
current_state = 1
pointer = 0
number = 0
while current_state != 0:
    if current_state and data_input[pointer] == 1:
        data_input[pointer] = 1
        pointer += 1
        current_state = 2
    if current_state == 2 and data_input[pointer] == 0:
        data_input[pointer] = 0
        pointer += 1
        current_state = 2
    if current_state == 2 and data_input[pointer]== 1:
        data_input[pointer] = 0
        pointer += 1
        current_state = 3
    if current_state == 3 and data_input[pointer] == 0:
        data_input[pointer] = 0
        pointer += 1
        current_state = 3
    if current_state == 3 and data_input[pointer]== 1:
        data_input[pointer] = 1
        pointer -= 1
        current_state = 4
    if current_state == 4 and data_input[pointer] == 0:
        data_input[pointer] = 1
        pointer += 1
        current_state = 0
for data in data_input:
    if data == 0:
        number += 1
print(data_input)
print(number)