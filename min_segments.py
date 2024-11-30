def min_segments(total_length, length_1, length_2):
    min_count = None
    best_combo = (0, 0)

    for count_1 in range(int(total_length // length_1) + 1):
        # Рассчитываем оставшуюся длину после отрезков длиной length_1
        remaining_length = total_length - count_1 * length_1

        if remaining_length % length_2 == 0:
            count_2 = int(remaining_length // length_2)
            total_segments = count_1 + count_2

            if min_count is None or total_segments < min_count:
                min_count = total_segments
                best_combo = (count_1, count_2)

    return best_combo, min_count

total_lenght = 23
lenght_1 = 1.5
lenght_2 = 2

best_combo, min_count = min_segments(total_lenght,
                                      lenght_1,
                                      lenght_2)


if min_count is not None:
    print(f"Min quantity of segments: {min_count}")
    print(f"Segments of {lenght_1} meters: {best_combo[0]}")
    print(f"Segments of {lenght_2} meters: {best_combo[1]}")
else:
    print("It's impossible to slice with this segmets sizes")
