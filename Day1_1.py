with open('day1-1_input_data.txt') as input_data:
    calibration_vals = []
    for line in input_data:

        digit_chars = [char for char in line if char.isdigit()]
        first_last = digit_chars[0] + digit_chars[-1]
        calibration_vals.append(first_last)
        

    calibration_vals = [int(i) for i in calibration_vals]
    total = sum(calibration_vals)
    print("SUM =", total)