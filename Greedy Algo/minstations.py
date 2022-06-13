plat_count = 1
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
my_dict = {}

for i in range(len(arr)):
	my_dict[arr[i]] = 1
	my_dict[dep[i]] = 0

sorted_list = sorted(my_dict.items())
max_count = 0
count = 0

for i in range(len(sorted_list)):
	if sorted_list[i][1] == 1:
		count += 1
	else:
		count -= 1
	if count > max_count:
		max_count = count

print(max_count)