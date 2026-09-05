
raw_data = " 100, 25, 10, 50, 25, 100, 50, 75, 10 "
# Expectation: [10, 25, 50, 75, 100]
data = []
raw_data_list = raw_data.strip().split(', ')
print(raw_data_list)
for raw in raw_data_list:
    data_int = int(raw)
    data.append(data_int)
dataset = set(data)
set_sorted = sorted(dataset)
print(set_sorted)