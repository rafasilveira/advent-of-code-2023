import re

numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solution(file_path="input/puzzle.txt"):
    file = open(file_path, "r")

    sum_calibration_values = 0

    for line in file:
        digits = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        numeric_digits = [int(x) if x.isdigit() else numbers[x] for x in digits]
        calibration_value = f"{numeric_digits[0]}{numeric_digits[-1]}"
        print(f"original line: {line.strip()}")
        print(f"digits: {numeric_digits}")
        print(f"calibration value: {calibration_value}\n")
        sum_calibration_values += int(calibration_value)

    file.close()

    print(f"sum of calibration values: {sum_calibration_values}")


if __name__ == "__main__":
    solution()
