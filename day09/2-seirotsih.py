from collections import Counter


def generate_sequences(history, sequences=[]):
    next_list = []
    updated_sequences = sequences
    for i in range(1, len(history)):
        current = history[i]
        prev = history[i - 1]
        next_list.append(current - prev)
    counter = Counter(next_list)
    updated_sequences.append(next_list)
    if counter.get(0) and len(counter.items()) == 1:
        return updated_sequences
    else:
        return generate_sequences(next_list, updated_sequences)


def solution(file_path="input/puzzle.txt"):
    histories = []
    predicted_values = []
    with open(file_path, "r") as file:
        for line in file:
            history = [int(x) for x in line.split()]
            history.reverse()
            histories.append(history)

    for history in histories:
        sequences = generate_sequences(history, [history])
        sequences.reverse()
        for i in range(len(sequences) - 1):
            current_sequence = sequences[i]
            next_sequence = sequences[i + 1]
            sequences[i + 1].append(next_sequence[-1] + current_sequence[-1])

        predicted_value = sequences[-1][-1]
        predicted_values.append(predicted_value)

    print(f"sum: {sum(predicted_values)}")


if __name__ == "__main__":
    solution()
