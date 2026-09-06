raw_data = " 100, 25, 10, 50, 25, 100, 50, 75, 10 "
# Expectation: [10, 25, 50, 75, 100]
dataset = set([int(angka) for angka in raw_data.strip().split(', ')])
set_sorted = sorted(dataset)
print(set_sorted)