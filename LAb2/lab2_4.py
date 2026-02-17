temp = map(int, input().split())
temp_list = list(temp)
temP_max = max(temp_list)
temp_min = min(temp_list)

avg = sum(temp_list) / len(temp_list)
ab_avg = []
for temp in temp_list:
    if temp > avg:
        ab_avg.append(temp)

print(temP_max)
print(temp_min)
print(avg)
print(len(ab_avg))
    