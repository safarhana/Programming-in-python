def count_elements(lst):
    counts = {}

    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    for key, value in counts.items():
        print(f"{key}: {value}")

sample = [10, 20, 30, 30, 30, 20, 40]
count_elements(sample)

