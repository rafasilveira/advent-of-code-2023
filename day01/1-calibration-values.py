import re


def solution(file_path="input/puzzle.txt"):
    file = open(file_path, "r")

    sum_calibration_values = 0

    for line in file:
        digits = re.findall(r"\d", line)
        calibration_value = f"{digits[0]}{digits[-1]}"
        print(f"original line: {line.strip()}")
        print(f"digits: {digits}")
        print(f"calibration value: {calibration_value}\n")
        sum_calibration_values += int(calibration_value)

    file.close()

    print(f"sum of calibration values: {sum_calibration_values}")


if __name__ == "__main__":
    solution()
