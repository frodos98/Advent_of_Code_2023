numbers_dict = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

with open('day1_input_data.txt') as input_data:
    calibration_vals = []
    for line in input_data:
        list_of_numbers = []
        for i in range(0,len(line)+1,1):
            for j in range(1,i+6,1):
                key=line[i:j]
                if key.isdigit():
                    list_of_numbers.append(key)
                else:
                    if key in numbers_dict:
                        list_of_numbers.append(numbers_dict[key])
                    else:
                        pass
        digit_chars = [str(n) for n in list_of_numbers]
        first_last = digit_chars[0] + digit_chars[-1]
        calibration_vals.append(first_last)

    calibration_vals = [int(i) for i in calibration_vals]
    total = sum(calibration_vals)
    print("SUM =", total)